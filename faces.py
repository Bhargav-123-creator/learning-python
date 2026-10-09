def main():
   x = input("")
   print(convert(x))

def convert(text):
   text = text.replace(":)", "🙂")
   text = text.replace(":(", "🙁")
   return text


main()