user = input("Greeting: ").strip().lower()

if user.startswith("hello"):
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")
