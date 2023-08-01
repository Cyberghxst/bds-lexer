# BDScript Lexer
This is a BDScript lexer written in Python.

⚠️ This code can contain bugs, use at your own risk.
⚠️ If you use this code, please give credits to this repo.

## Example
```py
from tokenizer import Tokenizer

code = "Hi good morning! $print[THIS IS PRINTABLE] THIS ISN'T"
reader = Tokenizer()
tokens = reader.build_tokens(code)
print(tokens)
```