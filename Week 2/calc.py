def main():
    a = input("Expression:")
    x , y , z = a.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
         c = (x+z)
         print(f"{c:.1f}")
    elif y == "-":
         c = (x-z)
         print(f"{c:.1f}")
    elif y == "*":
         c = (x*z)
         print(f"{c:.1f}")
    elif y == "/":
        if z !=0:
            c = (x/z)
            print(f"{c:.1f}")
        else:
            print("error")
    else:
        print("error")
main()
        
