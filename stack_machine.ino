const int STACK_SIZE = 10;
float stack[STACK_SIZE];
int top = -1;  

void push(float value) {
  if (top < STACK_SIZE - 1) {
    top++;
    stack[top] = value;
  }
}

float pop() {
  if (top >= 0) {
    float value = stack[top];
    top--;
    return value;
  }
  return 0.0; 
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String instruction = Serial.readStringUntil('\n');
    executeInstruction(instruction);
  }
}

void executeInstruction(String instruction) {
  instruction.trim();
  Serial.print("Received: ");
  Serial.println(instruction);

  if (instruction.startsWith("PUSH")) {
    float value = instruction.substring(5).toFloat();
    push(value);
  } else if (instruction == "POP") {
    float value = pop();
    Serial.print("Popped: ");
    Serial.println(value);
  } else if (instruction == "ADD") {
    if (top >= 1) {
      float b = pop();
      float a = pop();
      push(a + b);
    } else {
      Serial.println("Not enough operands for ADD");
    }
  } else if (instruction == "MUL") {
    if (top >= 1) {
      float b = pop();
      float a = pop();
      push(a * b);
    } else {
      Serial.println("Not enough operands for MUL");
    }
  } else if (instruction == "DIV") {
    if (top >= 1) {
      float b = pop();
      float a = pop();
      if (b != 0) {
        push(a / b);
      } else {
        Serial.println("Division by zero");
      }
    } else {
      Serial.println("Not enough operands for DIV");
    }
  } else {
    Serial.println("Invalid instruction");
  }

  Serial.print("Stack: [");
  for (int i = 0; i <= top; i++) {
    Serial.print(stack[i]);
    if (i < top) {
      Serial.print(", ");
    }
  }
  Serial.println("]");
}