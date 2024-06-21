a, b, c = input("Expression: ").split()

a, c = int(a), int(c)
result = eval(f"{a} {b} {c}")

print(f"{result:.1f}")
