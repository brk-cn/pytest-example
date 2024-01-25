def main():
  x = int(input("X: "))
  y = int(input("Y: "))

  print("choose an operand")
  print("'+' for addition")
  print("'-' for subtraction")
  print("'*' for multiplication")
  print("'/' for division")

  operand = input("operand: ")

  print(calculator(x, y, operand))

def calculator(x, y, operand):
  if not isinstance(x, int) or not isinstance(y, int):
    raise ValueError("Invalid input")

  if operand not in ['+', '-', '*', '/']:
    raise ValueError("Invalid operand")
    
  if operand == '+':
    return x + y
  elif operand == '-':
    return x - y
  elif operand == '*':
    return x * y
  elif operand == '/':
    if y != 0:
      return x / y
    else:
      raise ZeroDivisionError("The divisor cannot be 0")

if __name__ == "__main__":
  main()