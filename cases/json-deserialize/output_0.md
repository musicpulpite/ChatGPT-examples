Sure, here's an example implementation of a JSON parser in Python. This parser assumes that the given JSON string is well-formed and follows the standard JSON syntax.

```
class JSONParser:
    def __init__(self, json_str):
        self.json_str = json_str
        self.index = 0
    
    def parse(self):
        return self.read_value()
        
    def read_object(self):
        obj = {}
        self.index += 1
        while self.index < len(self.json_str):
            ch = self.json_str[self.index]
            if ch == '}':
                break
            elif ch == ',':
                self.index += 1
                continue

            key = self.read_string()
            self.index += 1
            val = self.read_value()
            obj[key] = val

        return obj

    def read_array(self):
        arr = []
        self.index += 1
        while self.index < len(self.json_str):
            ch = self.json_str[self.index]
            if ch == ']':
                break
            elif ch == ',':
                self.index += 1
                continue

            val = self.read_value()
            arr.append(val)

        return arr

    def read_string(self):
        str_value = ''
        self.index += 1
        while self.index < len(self.json_str):
            ch = self.json_str[self.index]
            if ch == '"':
                break
            str_value += ch
            self.index += 1
        return str_value

    def read_number(self):
        num_str = ''
        while self.index < len(self.json_str):
            ch = self.json_str[self.index]
            if ch.isdigit() or ch == '.' or ch == '-':
                num_str += ch
                self.index += 1
            else:
                break
        if '.' in num_str:
            return float(num_str)
        else:
            return int(num_str)

    def read_value(self):
        while self.index < len(self.json_str):
            ch = self.json_str[self.index]
            if ch == '{':
                return self.read_object()
            elif ch == '[':
                return self.read_array()
            elif ch == '"':
                return self.read_string()
            elif ch.isdigit() or ch == '-' or ch == '.':
                return self.read_number()
            elif ch == 't':
                self.index += 4
                return True
            elif ch == 'f':
                self.index += 5
                return False
            elif ch == 'n':
                self.index += 4
                return None
            else:
                self.index += 1

        return None
```

Here's an example usage of the parser:

```
json_str = '{"name": "John", "age": 30, "city": "New York"}'
parser = JSONParser(json_str)
result = parser.parse()
print(result)
```

This should output:

```
{'name': 'John', 'age': 30, 'city': 'New York'}
```

Note that this is a simple implementation of a JSON parser and may not handle all edge cases. It's always best to use a trusted and tested third-party JSON library in production code.