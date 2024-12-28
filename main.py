def main():

    print("Welcome to the Rollercoaster!")
    height = input("What's your height in cm? ")
    height_float = float(height)

    if height_float >= 120:
          print("Yes, you can ride the rollercoaster")
    else:
          print("No, you can't ride the rollercoaster")
    

if __name__=="__main__":
        main()