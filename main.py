from tokenizer import Tokenizer

code = """
THIS IS A TEXT
$print[HELLO WORLD FROM BDS LEXER]
THIS IS ANOTHER TEXT
"""

# New instance
tk = Tokenizer()

# Reading code
tokens = tk.build_tokens(code)

# Showing tokens
print(tokens)