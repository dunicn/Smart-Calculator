import re


class Calculator:

    def __init__(self):
        self.operations = ("+", "-", "/", "*", "^")
        self.variables = dict()

    def int_or_value(self, user_input):
        if user_input.isnumeric():
            return user_input
        elif user_input.isalpha():
            return self.dict_check(user_input)

    def operator_plus_minus(self, operator):
        return operator == "+" or operator == "-"

    def operator_multiplication_division(self, operator):
        return operator == "*" or operator == "/"

    def operator_square(self, operator):
        return operator == "^"

    def priority_check(self, incoming, top):
        if self.operator_plus_minus(incoming):
            return False
        elif self.operator_multiplication_division(incoming) and not self.operator_plus_minus(top):
            return False
        elif self.operator_multiplication_division(incoming) and self.operator_plus_minus(top):
            return True
        elif self.operator_square(incoming):
            return True
        return True


    def infix_to_postfix(self, text):
        new_stack = []
        operation_stack = []
        for char in text:
            if char.isdigit():
                new_stack.append(char)
            elif char in self.variables:
                new_stack.append(char)
            elif char in self.operations and (operation_stack == [] or operation_stack[-1] == "("):
                operation_stack.append(char)
            elif char == ")":
                while operation_stack and operation_stack[-1] != "(":
                    new_stack.append(operation_stack.pop())
            elif char == "(":
                operation_stack.append(char)
            elif char in self.operations and operation_stack[-1] in self.operations:
                if self.priority_check(char, operation_stack[-1]):
                    operation_stack.append(char)
                elif self.priority_check(char, operation_stack[-1]) is False:
                    while operation_stack and self.priority_check(char, operation_stack[-1]) is False or operation_stack and operation_stack[-1] == "(":

                        new_stack.append(operation_stack.pop())
                    operation_stack.append(char)


        while operation_stack:
            popped_operator = operation_stack.pop()
            new_stack.append(popped_operator)

        return new_stack

    def operation_method(self, a, b, operator):
        a = int(a)
        b = int(b)
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        elif operator == "^":
            return pow(a, b)


    def final_calculator(self, postfix):
        result = []
        for element in postfix:
            if element.isdigit():
                result.append(element)
            elif element in self.variables:
                result.append(self.dict_check(element))
            elif element in self.operations:
                b = result.pop()
                a = result.pop()
                result.append(self.operation_method(a, b, element))
        return int(result[0])

    def identifier_check(self, input_string):
        if input_string.isalpha():
            return True

    def split_identifier_check(self, user_input):
        input_check = [x.strip() for x in user_input.split("=")]
        if len(input_check) > 2:
            print("Invalid assignment")
        elif not self.identifier_check(input_check[0]):
            print("Invalid identifier")
        elif input_check[1] in self.variables:
            self.variables[input_check[0]] = self.variables.get(input_check[1])
        elif not input_check[1].isnumeric() and input_check[1] not in self.variables:
            print("Invalid assignment")
        else:
            self.variables[input_check[0]] = input_check[1]

    def dict_check(self, user_input):
        if user_input not in self.variables:
            return "Unknown variable"
        else:
            return self.variables[user_input]

    def parenthesis_check(self, text):
        parenthesis_list = []
        for character in text:
            if character == "(":
                parenthesis_list.append(character)
            elif character == ")":
                if not parenthesis_list:
                    return False
                else:
                    parenthesis_list.pop()

        if not parenthesis_list:
            return True
        else:
            return False

    def input_check(self):
        while True:
            text = input()
            if text.startswith("+"):
                text = text.replace("+", "")
            if text.startswith(" "):
                text = text.replace(" ", "")
            if text.startswith("/") and text != "/help" and text != "/exit":
                print("Unknown command")
            elif "++" in text:
                text = re.sub("\++", "+", text)
            elif "=" in text or text in self.variables or text.isalpha():
                if text.isalpha():
                    print(self.dict_check(text))
                else:
                    self.split_identifier_check(text)
            elif text.endswith("-") \
                    or text.endswith("+") \
                    or text.endswith("*") \
                    or text.endswith("/") \
                    or text.endswith("^"):
                print("Invalid expression")
            elif text.startswith(")") or text.endswith("("):
                print("Invalid expression")
            elif "//" in text or "**" in text:
                print("Invalid expression")
            elif not self.parenthesis_check(text):
                print("Invalid expression")
            elif text == '/help':
                print('The program calculates the sum of numbers')
            elif text == '/exit':
                print('Bye!')
                exit()
            elif text == '':
                continue
            else:
                if "-+" in text:
                    text = re.sub("\-\+", "-", text)
                if "--" in text:
                    text = re.sub("\\--", "+", text)
                if "++" in text:
                    text = re.sub("\++", "+", text)
                if "+-" in text:
                    text = re.sub("\+-", "-", text)
                if "+" in text:
                    text = re.sub("\+", " + ", text)
                if "-" in text:
                    text = re.sub("\-", " - ", text)
                if "*" in text:
                    text = re.sub("\*", " * ", text)
                if "/" in text:
                    text = re.sub("\/", " / ", text)
                if "^" in text:
                    text = re.sub("\^", " ^ ", text)
                if "(" in text:
                    text = re.sub("\(", " ( ", text)
                if ")" in text:
                    text = re.sub("\)", " ) ", text)

                return list(text.split())  # list of input

    def main(self):
        while True:
            infix_list = self.input_check()

            postfix = self.infix_to_postfix(infix_list)
            print(self.final_calculator(postfix))


test = Calculator()
test.main()
