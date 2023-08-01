from tokenizer import Tokenizer

code = """
$print[HELLO WORLD FROM BDS LEXER]
"""

# New instance
tk = Tokenizer()

# Reading code
tokens = tk.build_tokens(code)

# Showing tokens
print(tokens)