# Stack Machine in Python

This repository contains a simple implementation of a stack machine in Python. A stack machine is a type of computer processor design that relies on a stack to hold values, rather than a set of registers. This stack machine supports basic arithmetic operations, stack operations, and some advanced features.

## Usage

Create an instance of the `StackMachine` class and call its `execute` method with each instruction in the program. Alternatively, load a list of instructions using the `load_program` method.

Example:

```python
sm = StackMachine()
sm.load_program([
    "PUSH 5",
    "PUSH 3",
    "DUP",
    "ADD",
    "SWAP",
    "PRINT"  # Outputs: 5
])
```

In this example, the program pushes `5` and `3` onto the stack, duplicates the `3`, adds the duplicate `3` to the `3` already on the stack (resulting in `6`), swaps the `6` and the `5` (so `5` is on top), and then prints the top value of the stack, which is `5`.

## Instructions

The following instructions are supported:

- `PUSH <n>`: Pushes the number `<n>` onto the stack.
- `POP`: Removes the top value from the stack and discards it.
- `DUP`: Duplicates the top value on the stack.
- `SWAP`: Swaps the top two values on the stack.
- `ADD`: Removes the top two values from the stack, adds them together, and pushes the result back onto the stack.
- `SUB`: Removes the top two values from the stack, subtracts the second one from the first, and pushes the result back onto the stack.
- `MUL`: Removes the top two values from the stack, multiplies them together, and pushes the result back onto the stack.
- `DIV`: Removes the top two values from the stack, divides the second one by the first (throwing an error if the first is zero), and pushes the result back onto the stack.
- `PRINT`: Prints the top value on the stack.

## Loading a Program

A program can be loaded as a list of instructions using the `load_program` method of the `StackMachine` class. Each instruction in the list should be a string.

Example:

```python
program = [
    "PUSH 5",
    "PUSH 3",
    "DUP",
    "ADD",
    "SWAP",
    "PRINT"
]
sm = StackMachine()
sm.load_program(program)
```

This will execute the program in the same way as the earlier example.

## Testing

A simple test program is included in the `stack_machine.py` file. This program demonstrates basic usage of the stack machine.

To run the test program, execute the `stack_machine.py` file using a Python interpreter.

## Requirements

Python 3.6 or higher is required to run this program.