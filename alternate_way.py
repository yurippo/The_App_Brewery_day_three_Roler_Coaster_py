def main():

    print("Welcome to the Rollercoaster!")
    height = input("What's your height in cm? ")
    height_float = float(height)
    
    
    if height_float >= 120:
            print("Yes, you can ride the rollercoaster")
                  
            age = input("What's your age? ")
            age_int = int(age)

            if age_int < 12:
                  bill = 5
                  print("child tickets are $5")
                  
                        
            elif age_int >= 12 and age_int <= 18:
                  bill = 7
                  print("Youth tickets are $7")

            elif age_int >= 45 and age_int <= 55: #I could also use 45 <= age_int <= 55  a simpler way to do it
                  print("Midlife crisis Everything is going to be ok. Have a free ride on us!")
                  bill = 0                  
                  
            
            else:
                  bill = 12
                  print("Adult tickets are $12")
                  
            wants_photo = input("Do you want a photo taken? y or n ")
            wants_photo_to_lower = wants_photo.lower()
            if wants_photo_to_lower == "y":
                  bill += 3
                  print(f"Please pay extra $3 for the photo. The total bill is ${bill}")
            else:
                  print(f"No problem! The total bill is ${bill} enjoy the ride")
          
    else:
          print("No, you can't ride the rollercoaster")
          print("Sorry you have to grow taller before you can ride")
    

if __name__=="__main__":
        main()