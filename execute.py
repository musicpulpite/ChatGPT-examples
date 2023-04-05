import os
import argparse
import json
from multiprocessing import Pool

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai


openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

def execute_case(case_directory):
  with open(f'cases/{case_directory}/input.json') as json_file:
    input_messages = json.load(json_file)
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=input_messages
    )
    return response

def main():
  parser = argparse.ArgumentParser("Execute and record ChatGPT examples")
  parser.add_argument("--case", help="Which example case to run, omit to run all")
  args = parser.parse_args()
  example_case = args.case

  case_directories = []
  all_case_directories = [c for c in os.listdir('cases') if os.path.isdir(f'cases/{c}')]
  if example_case is None:
    case_directories = all_case_directories
  else:
    if example_case in all_case_directories:
      case_directories = [example_case]
    else:
      raise Exception('specified case does not exist')
  
  print(f'Executing {len(case_directories)} cases: {case_directories}')
    
  with Pool(len(case_directories)) as pool:
    responses = pool.map(execute_case, case_directories)

  for idx, case_directory in enumerate(case_directories):
      response = responses[idx]
      with open(f'cases/{case_directory}/output_complete.json', "w") as outfile:
        response_json = json.dumps(response, indent=4)
        outfile.write(response_json)
      for idx, choice in enumerate(response["choices"]):
        with open(f'cases/{case_directory}/output_{idx}.md', "w") as outfile:
          outfile.write(choice["message"]["content"])



if __name__ == "__main__":
  main()