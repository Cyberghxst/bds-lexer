import re

class TokenType:
    FunctionName = "FUNCTION_NAME"
    FunctionParams = "FUNCTION_PARAMETERS"
    Text = "TEXT"

class Lexer:
    def read(self, input: str):
        """
        Read and split the raw BDS code into mini-tokens to build the tokens.

        Parameters
        ----------
        input: str
            The raw BDS code to read.
        """
        depth: int = 0
        tokens = []
        type: str = TokenType.Text
        for i, char in enumerate(input):
            if char == "[": depth += 1
            elif char == "]": depth -= 1
            if char == "$" and re.match(pattern="[a-zA-Z]", string=input[i + 1]) and input[i + 1] != None:
                type = TokenType.FunctionName
            elif (char == " " or char == "\n") and type == TokenType.FunctionName and depth == 0:
                type = TokenType.Text
            elif char == "[" and type == TokenType.FunctionName:
                type = TokenType.FunctionParams
            elif (char == "]" or char == " " or char == "\n") and type == TokenType.FunctionParams and depth == 0:
                tokens.append({ "value": char, "type": type })
                type = TokenType.Text
                continue
            tokens.append({ "value": char, "type": type })
        return tokens