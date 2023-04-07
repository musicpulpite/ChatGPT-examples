import os
import argparse
import json

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from colorama import init, Fore, Back, Style

init(autoreset=True)

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(lines):
    prompt = [
        {"role": "system", "content": "Given the following command line history and the current command that failed, what should the correct next command be?"},
        {"role": "system", "content": "Format the content of your message response as a JSON string with a key of 'command' and value of the corrected command and a key of 'reason' with a value of the reason for your correction. For example: {'command': 'ls -l', 'reason': 'missing -l'}"},
        {"role": "system", "content": "The returned json string must use double quotes and not single quotes so that it can be parsed using json.loads()."},
        *[{"role": "user", "content": line} for line in lines],
    ]
    return prompt

global corrected_command
global verbose

def log(msg):
    if verbose:
        print(Fore.GREEN + msg + Style.RESET_ALL)

def main():
    global verbose
    global corrected_command

    parser = argparse.ArgumentParser()
    parser.add_argument("--histfile")
    parser.add_argument("--verbose", default=False, action="store_true")
    args = parser.parse_args()
    histfile_path = args.histfile
    verbose = args.verbose

    if not os.path.exists(histfile_path):
        return

    with open(histfile_path, "r") as f:
        lines = f.readlines()
        lines = lines[0:min(len(lines), 10)]
        log("History: " + str(lines))
        prompt = build_prompt(lines)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=prompt
            )
            corrected_command = response["choices"][0]["message"]["content"]
            corrected_command = json.loads(corrected_command)  
        except Exception as e:
            print("Error while calling OpenAI API")

        print(corrected_command["command"], Style.DIM + f'({corrected_command["reason"]})' + Style.RESET_ALL, end="")
        try:
            input()
        except:
            return
        os.system(corrected_command["command"])

if __name__ == "__main__":
    main()