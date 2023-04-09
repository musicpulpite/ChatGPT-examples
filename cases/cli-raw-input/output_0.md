Sure, here's an example code that prompts the user for input using prompt_toolkit library in Python, and allows editing of default value:

```python
from prompt_toolkit import prompt, PromptSession

# create a PromptSession object
session = PromptSession()

# Set default value for the prompt
default_value = "default_value"

# Use the prompt function to get input. Set the default value and insert cursor before it
user_input = session.prompt(f"Enter Input: ", default=default_value, default_text_before_cursor = True)

# Print the entered input
print(f"You entered: {user_input}")
```

In this code, we first import `prompt` and `PromptSession` from the `prompt_toolkit` library. We then store a `PromptSession` object in the `session` variable.

We set a default value for the prompt in the `default_value` variable. The `prompt` function is used to get input from the user with a prompt message of "Enter Input:". We pass the `default` parameter to the `prompt` function with the `default_value` variable, so that the default value is displayed on the prompt. We also set the `default_text_before_cursor` parameter to `True` so that the cursor is placed before the default value, allowing the user to edit it if necessary.

Finally, we print the entered input with a message "You entered: ".

You can run this script from the command line and try it out.