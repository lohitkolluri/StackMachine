class StackMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise RuntimeError("Attempted to pop an empty stack")
        return self.stack.pop()

    def add(self):
        if len(self.stack) < 2:
            raise RuntimeError("Attempted to add with less than two values on the stack")
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a + b)

    def subtract(self):
        if len(self.stack) < 2:
            raise RuntimeError("Attempted to subtract with less than two values on the stack")
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b - a)

    def multiply(self):
        if len(self.stack) < 2:
            raise RuntimeError("Attempted to multiply with less than two values on the stack")
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a * b)

    def divide(self):
        if len(self.stack) < 2:
            raise RuntimeError("Attempted to divide with less than two values on the stack")
        a = self.stack.pop()
        b = self.stack.pop()
        if a == 0:
            raise RuntimeError("Attempted to divide by zero")
        self.stack.append(b / a)

    def print(self):
        if not self.stack:
            raise RuntimeError("Attempted to print an empty stack")
        print(self.stack[-1])

    def execute(self, instruction):
        if instruction == "ADD":
            self.add()
        elif instruction == "SUB":
            self.subtract()
        elif instruction == "MUL":
            self.multiply()
        elif instruction == "DIV":
            self.divide()
        elif instruction == "PRINT":
            self.print()
        elif instruction.startswith("PUSH"):
            _, num = instruction.split()
            self.push(int(num))
        elif instruction == "POP":
            self.pop()
        else:
            raise RuntimeError(f"Unrecognized instruction: {instruction}")


def test_program():
    sm = StackMachine()
    sm.execute("PUSH 5")
    sm.execute("PUSH 3")
    sm.execute("ADD")
    sm.execute("PRINT")  # Should print 8

test_program()