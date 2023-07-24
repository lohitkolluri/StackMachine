import tkinter as tk
from tkinter import messagebox

class StackMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise RuntimeError("Attempted to pop an empty stack")
        return self.stack.pop()

    def dup(self):
        if not self.stack:
            raise RuntimeError("Attempted to duplicate an empty stack")
        self.stack.append(self.stack[-1])

    def swap(self):
        if len(self.stack) < 2:
            raise RuntimeError("Attempted to swap with less than two values on the stack")
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)

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

    def execute(self, instruction):
        if instruction == "DUP":
            self.dup()
        elif instruction == "SWAP":
            self.swap()
        elif instruction == "ADD":
            self.add()
        elif instruction == "SUB":
            self.subtract()
        elif instruction == "MUL":
            self.multiply()
        elif instruction == "DIV":
            self.divide()
        elif instruction.startswith("PUSH"):
            _, num = instruction.split()
            self.push(int(num))
        elif instruction == "POP":
            self.pop()
        else:
            raise RuntimeError(f"Unrecognized instruction: {instruction}")

    def load_program(self, program):
        for instruction in program:
            self.execute(instruction)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.sm = StackMachine()

    def create_widgets(self):
        self.instruction_entry = tk.Entry(self)
        self.instruction_entry.pack(side="top")

        self.execute_button = tk.Button(self)
        self.execute_button["text"] = "Execute"
        self.execute_button["command"] = self.execute_instruction
        self.execute_button.pack(side="top")

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button["command"] = self.reset
        self.reset_button.pack(side="top")

        self.stack_label = tk.Label(self, text="Stack: []")
        self.stack_label.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def execute_instruction(self):
        instruction = self.instruction_entry.get()
        try:
            self.sm.execute(instruction)
            self.stack_label["text"] = f"Stack: {self.sm.stack}"
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset(self):
        self.sm = StackMachine()  # Reset the StackMachine
        self.instruction_entry.delete(0, 'end')  # Clear the instruction entry field
        self.stack_label["text"] = "Stack: []"  # Reset the stack label

root = tk.Tk()
app = Application(master=root)
app.mainloop()