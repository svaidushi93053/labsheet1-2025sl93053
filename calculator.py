def add(a,b):
 return a+b

def multiply(a,b):
 return a*b

def subtract(a,b):
  return a-b


def divide(a,b):
  if b==0:
    return None
  return a/b

if __name__ == "__main__":
    print("=== Calculator Results ===")
    print("Add      10 + 5 =", add(10, 5))
    print("Subtract 10 - 5 =", subtract(10, 5))
    print("Multiply 10 * 5 =", multiply(10, 5))
    print("Divide   10 / 5 =", divide(10, 5))


