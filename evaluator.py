def tokenize(text):
    tokens = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == " ":
            i += 1
        elif ch in "+-*/()":
            tokens.append(ch)
            i += 1
        elif ch.isdigit() or ch == ".":
            number = ""
            while i < len(text) and (text[i].isdigit() or text[i] == "."):
                number += text[i]
                i += 1
            try:
                tokens.append(float(number))
            except ValueError:
                raise ValueError("Invalid number: " + number)
        else:
            raise ValueError("Invalid character: " + ch)
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def parse(self):
        if len(self.tokens) == 0:
            raise ValueError("Empty expression")
        result = self.expression()
        if self.current() is not None:
            raise ValueError("Unexpected token: " + str(self.current()))
        return result


    def expression(self):
        result = self.term()
        while self.current() == "+" or self.current() == "-":
            op = self.current()
            self.pos += 1
            right = self.term()
            if op == "+":
                result = result + right
            else:
                result = result - right
        return result

    def term(self):
        result = self.factor()
        while self.current() == "*" or self.current() == "/":
            op = self.current()
            self.pos += 1
            right = self.factor()
            if op == "*":
                result = result * right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result = result / right
        return result

    def factor(self):
        token = self.current()

        if token is None:
            raise ValueError("Unexpected end of expression")

        if token == "-":
            self.pos += 1
            return -self.factor()

        if token == "(":
            self.pos += 1
            result = self.expression()
            if self.current() != ")":
                raise ValueError("Missing closing parenthesis")
            self.pos += 1
            return result

        if isinstance(token, float):
            self.pos += 1
            return token

        raise ValueError("Unexpected token: " + str(token))


def evaluate(text):
    tokens = tokenize(text)
    parser = Parser(tokens)
    return parser.parse()


def format_result(result):
    result = round(result, 10)
    if result.is_integer():
        return str(int(result))
    return str(result)


def main():
    print("Simple Expression Evaluator")
    print("Type 'exit' to quit.")
    while True:
        text = input("> ").strip()
        if text.lower() == "exit":
            break
        if text == "":
            continue
        try:
            result = evaluate(text)
            print(format_result(result))
        except ZeroDivisionError:
            print("Error: division by zero")
        except ValueError as e:
            print("Error:", e)
        except RecursionError:
            print("Error: expression is too deeply nested")
    print("Bye!")


if __name__ == "__main__":
    main()
