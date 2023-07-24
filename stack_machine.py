class StackMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def add(self):
        a = self.pop()
        b = self.pop()
        self.push(a + b)

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.push(a - b)

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.push(a * b)

    def div(self):
        a = self.pop()
        b = self.pop()
        self.push(a // b)

    def halt(self):
        exit()

def main():
    machine = StackMachine()
    machine.push(1)
    machine.push(2)
    machine.add()
    print(machine.pop())

if __name__ == "__main__":
    main()