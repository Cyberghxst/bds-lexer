from lexer import Lexer

class Tokenizer:
    """
    Read and split BDS code into tokens.
    """
    def build_tokens(self, code):
        mini_tokens = Lexer().read(code)
        tokens = []
        temp_token = {
            "content": "",
            "type": "Text"
        }
        for i, token in enumerate(mini_tokens):
            if "FUNCTION" in token["type"]:
                if i == len(mini_tokens) - 1 or mini_tokens[i + 1]["type"] == "TEXT":
                    temp_token["content"] += token["value"]
                    temp_token["type"] = "FUNCTION"
                    tokens.append(temp_token)
                    temp_token = {
                        "content": "",
                        "type": "Text"
                    }
                else:
                    temp_token["content"] += token["value"]
            else:
                if i == len(mini_tokens) - 1 or "FUNCTION" in mini_tokens[i + 1]["type"]:
                    temp_token["type"] = "TEXT"
                    temp_token["content"] += token["value"]
                    tokens.append(temp_token)
                    temp_token = {
                        "content": "",
                        "type": "Text"
                    }
                else:
                    temp_token["content"] += token["value"]
        return tokens