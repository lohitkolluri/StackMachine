import tkinter as tk
from tkinter import messagebox

class StackMachine:
    def __init__(self):
        self.stack = []

    def execute(self, instruction):
        parts = instruction.split()
        command = parts[0]

        if command == "PUSH":
            if len(parts) != 2:
                raise ValueError("PUSH command requires one argument.")
            value = float(parts[1])
            self.stack.append(value)
        elif command == "POP":
            if len(self.stack) == 0:
                raise ValueError("Cannot POP from an empty stack.")
            self.stack.pop()
        elif command == "ADD":
            if len(self.stack) < 2:
                raise ValueError("ADD command requires at least two values on the stack.")
            result = self.stack.pop() + self.stack.pop()
            self.stack.append(result)
        elif command == "SUB":
            if len(self.stack) < 2:
                raise ValueError("SUB command requires at least two values on the stack.")
            b = self.stack.pop()
            a = self.stack.pop()
            result = a - b
            self.stack.append(result)
        elif command == "MUL":
            if len(self.stack) < 2:
                raise ValueError("MUL command requires at least two values on the stack.")
            result = self.stack.pop() * self.stack.pop()
            self.stack.append(result)
        elif command == "DIV":
            if len(self.stack) < 2:
                raise ValueError("DIV command requires at least two values on the stack.")
            b = self.stack.pop()
            a = self.stack.pop()
            result = a / b
            self.stack.append(result)
        elif command == "DUP":
            if len(self.stack) == 0:
                raise ValueError("Cannot DUP from an empty stack.")
            value = self.stack[-1]
            self.stack.append(value)
        elif command == "SWAP":
            if len(self.stack) < 2:
                raise ValueError("SWAP command requires at least two values on the stack.")
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        else:
            raise ValueError(f"Invalid command: {command}")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Stack Machine')
        self.master.geometry('300x200') # Set window size
        self.master.configure(bg='light grey') # Set background color
        self.pack(padx=10, pady=10) # Add padding around widgets
        self.create_widgets()
        self.sm = StackMachine()

    def create_widgets(self):
        self.instruction_entry = tk.Entry(self)
        self.instruction_entry.pack(side="top", fill='x', padx=5, pady=5)

        self.execute_button = tk.Button(self)
        self.execute_button["text"] = "Execute"
        self.execute_button["command"] = self.execute_instruction
        self.execute_button["bg"] = "skyblue" # Set button color
        self.execute_button.pack(side="top", fill='x', padx=5, pady=5)

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset"
        self.reset_button["command"] = self.reset
        self.reset_button["bg"] = "skyblue" # Set button color
        self.reset_button.pack(side="top", fill='x', padx=5, pady=5)

        self.help_button = tk.Button(self)
        self.help_button["text"] = "Help"
        self.help_button["command"] = self.show_help
        self.help_button["bg"] = "skyblue" # Set button color
        self.help_button.pack(side="top", fill='x', padx=5, pady=5)

        self.stack_label = tk.Label(self, text="Stack: []")
        self.stack_label.pack(side="top", fill='x', padx=5, pady=5)

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

    def show_help(self):
        help_text = """
        Stack Machine Help:
        
        This is a simple Stack Machine application. It simulates the behavior of a stack-based processor.
        You can enter instructions in the entry field and use the buttons to interact with the stack.

        Commands:
        - PUSH <value>: Pushes the specified value onto the stack.
        - POP: Removes the topmost value from the stack.
        - ADD: Pops the top two values from the stack, adds them, and pushes the result.
        - SUB: Pops the top two values from the stack, subtracts the second from the first, and pushes the result.
        - MUL: Pops the top two values from the stack, multiplies them, and pushes the result.
        - DIV: Pops the top two values from the stack, divides the first by the second, and pushes the result.
        - DUP: Duplicates the top value on the stack and pushes the duplicate.
        - SWAP: Swaps the positions of the top two values on the stack.

        Usage:
        1. Enter an instruction in the entry field (e.g., "PUSH 42", "ADD", "POP", etc.).
        2. Click the "Execute" button to execute the instruction. The current stack will be displayed below.
        3. To clear the stack and start over, click the "Reset" button.

        Note: The stack can only store numeric values (integers or floating-point numbers).

        Have fun experimenting with the Stack Machine!
        """
        messagebox.showinfo("Help", help_text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()