def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user = input()
    converted = convert(user)
    print(converted)

main()