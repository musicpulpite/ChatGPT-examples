import os

from prompt_toolkit import prompt

amended_command = prompt("Fix: ", default="cd ..")
os.system(amended_command)