def main():

    print("Welcome to the Rollercoaster!")
    height = input("What's your height in cm? ")
    height_float = float(height)
    age = input("What's your age? ")
    age_int = int(age)

    if height_float >= 120:
            if age_int < 12:
                  print("Yes, you can ride the rollercoaster")
                  photo = input("Do you want a photo taken? Y or N ")
                  if photo == "Y":
                        print("Please pay extra $3 for the photo")
                        print("The total bill is $8")
                  else:
                        print("Please pay $5")
                        
            elif age_int >= 12 and age_int <= 18:
                  print("Yes, you can ride the rollercoaster")
                  photo = input("Do you want a photo taken? Y or N ")
                  if photo == "Y":
                        print("Please pay extra $3 for the photo")
                        print("The total bill is $10")
                  else:
                        print("Please pay $7")
                  
            else:
                  print("Yes, you can ride the rollercoaster")
                  photo = input("Do you want a photo taken? Y or N ")
                  if photo == "Y":
                        print("Please pay extra $3 for the photo")
                        print("The total bill is $15")
                  else:
                        print("Please pay $12")
                  
          
    else:
          print("No, you can't ride the rollercoaster")
          print("Sorry you have to grow taller before you can ride")
    

if __name__=="__main__":
        main()