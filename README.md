# Stack Machine in Python

This repository contains a simple implementation of a stack machine in Python. A stack machine is a type of computer processor design that relies on a stack to hold values, rather than a set of registers. This stack machine supports basic arithmetic operations and stack operations.

## Usage

Create an instance of the `StackMachine` class and call its `execute` method with each instruction in the program.

Example:

```python
sm = StackMachine()
sm.execute("PUSH 5")
sm.execute("PUSH 3")
sm.execute("ADD")
sm.execute("PRINT")  # Outputs: 8
```

In this example, the program pushes `5` and `3` onto the stack, adds them together (removing them from the stack and pushing the result onto the stack), and then prints the result.

## Instructions

The following instructions are supported:

- `PUSH <n>`: Pushes the number `<n>` onto the stack.
- `POP`: Removes the top value from the stack and discards it.
- `ADD`: Removes the top two values from the stack, adds them together, and pushes the result back onto the stack.
- `SUB`: Removes the top two values from the stack, subtracts the second one from the first, and pushes the result back onto the stack.
- `MUL`: Removes the top two values from the stack, multiplies them together, and pushes the result back onto the stack.
- `DIV`: Removes the top two values from the stack, divides the second one by the first (throwing an error if the first is zero), and pushes the result back onto the stack.
- `PRINT`: Prints the top value on the stack.

Each instruction is executed by calling the `execute` method of the `StackMachine` class with the instruction as a string.

## Testing

A simple test program is included in the `stack_machine.py` file. This program demonstrates basic usage of the stack machine.

To run the test program, execute the `stack_machine.py` file using a Python interpreter.

## Requirements

Python 3.6 or higher is required to run this program.