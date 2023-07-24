# Stack Machine Application

The Stack Machine Application is a simple graphical user interface (GUI) that simulates the behavior of a stack-based processor. It allows users to execute instructions and manipulate a stack.

## Features

- Push numeric values onto the stack.
- Pop values from the top of the stack.
- Perform basic arithmetic operations on stack values (addition, subtraction, multiplication, division).
- Duplicate the top value on the stack.
- Swap the positions of the top two values on the stack.
- Reset the stack to its initial state.

## Prerequisites

- Python 3.x
- tkinter (included with Python standard library)

## How to Run

1. Clone this repository to your local machine.

2. Navigate to the repository directory.

3. Run the application using the following command:

```bash
python stack_machine.py
```

4. The Stack Machine GUI window will appear.

## Usage

1. Enter an instruction in the entry field and press Enter or click the "Execute" button to execute the instruction.

2. The current stack will be displayed below the buttons.

3. To clear the stack and start over, click the "Reset" button.

4. For more information about the available commands and usage, click the "Help" button.

## Command Instructions

- **PUSH <value>:** Pushes the specified numeric value onto the stack.
- **POP:** Removes the topmost value from the stack.
- **ADD:** Pops the top two values from the stack, adds them, and pushes the result onto the stack.
- **SUB:** Pops the top two values from the stack, subtracts the second from the first, and pushes the result onto the stack.
- **MUL:** Pops the top two values from the stack, multiplies them, and pushes the result onto the stack.
- **DIV:** Pops the top two values from the stack, divides the first by the second, and pushes the result onto the stack.
- **DUP:** Duplicates the top value on the stack and pushes the duplicate.
- **SWAP:** Swaps the positions of the top two values on the stack.

## History

The application stores the history of executed instructions during the session. The history is cleared when the application is closed.