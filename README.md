# Arduino Stack Machine Simulator

A simple Arduino sketch that simulates a stack machine, allowing you to execute stack-based operations via serial communication.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Examples](#examples)


## Introduction

This Arduino sketch provides a basic stack machine simulator, allowing you to push and pop values from a stack and perform arithmetic operations (addition, multiplication, and division) using simple commands. It's designed for educational purposes and can be used as a starting point for learning about stack-based systems and basic arithmetic operations.

## Features

- Push values onto the stack.
- Pop values from the stack.
- Perform addition, multiplication, and division operations.
- Error handling for stack underflow and division by zero.
- Interaction via the Arduino Serial Monitor.

## Requirements

- Arduino board (e.g., Arduino Uno)
- Arduino IDE or online IDE (e.g., Tinkercad for simulation)
- Serial communication tool (e.g., Arduino Serial Monitor, Tinkercad's Serial Monitor)

## Usage

1. Upload the provided Arduino sketch to your Arduino board using the Arduino IDE or compatible online platforms.
2. Open the Arduino Serial Monitor or use a serial communication tool if you're using Tinkercad.
3. Enter instructions in the Serial Monitor to interact with the stack machine. Supported commands include:
   - `PUSH <value>`: Push a floating-point value onto the stack.
   - `POP`: Pop the top value from the stack.
   - `ADD`: Perform addition on the top two stack values.
   - `MUL`: Perform multiplication on the top two stack values.
   - `DIV`: Perform division on the top two stack values (avoiding division by zero).
4. Observe the stack's current state and any operation results in the Serial Monitor.

## Examples

Here are some example instructions you can enter in the Serial Monitor:

- `PUSH 42`: Push the value 42 onto the stack.
- `PUSH 10`: Push the value 10 onto the stack.
- `ADD`: Perform addition on the top two stack values.
- `MUL`: Perform multiplication on the top two stack values.
- `DIV`: Perform division on the top two stack values.