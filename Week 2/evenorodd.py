def main():
    x = int(input("Enter a number"))
    evenodd(x)

def evenodd(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

main()
