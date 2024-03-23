def main():
  x = int(input("N: "))

  print(factorial(n))

def factorial(n):
  if not isinstance(n, int):
    raise ValueError("Invalid input")

  if n < 0:
    raise ValueError("Invalid input")

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  main()