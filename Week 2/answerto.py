def main():
    x = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    x = lower(x)
    if x == "42":
        print("Yes")
    elif x == "forty two":
        print("yes")
    elif x == ("forty-two"):
        print("yes")
    else:
        print("No")




def lower(text):
    return text.lower()

main()