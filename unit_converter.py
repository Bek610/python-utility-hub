
while True:
 print("Choose a unit to convert")
 print("1. Temperature")
 print("2. Distance")
 print("3. Weight")
 print("4. Time")
 print("5. Exit")


 choice = input("Enter your choice: ")
 if not choice.isdigit():
     print("Invalid choice! please enter a number")
     continue
 choice = int(choice)
 if choice == 1:
     print(" You chose temperature!")
     print("1. Celsius → Fahrenheit ")
     print("2. Fahrenheit → Celsius ")
     print("3. Celsius → Kelvin  ")
     print("4. Kelvin → Celsius ")
     temp_choice = input("Enter your choice: ")
     if not temp_choice.isdigit():
         print("Invalid choice! please enter a number")
         continue
     temp_choice = int(temp_choice)
     if temp_choice == 1:
         celsius = float(input("Enter your temperature in Celsius: "))
         fahrenheit= (celsius * 9/5) + 32
         print("Fahrenheit is", fahrenheit)
     elif temp_choice == 2:
         fahrenheit = float(input("Enter your temperature in Fahrenheit: "))
         celsius = (fahrenheit - 32) * 5/9
         print("Celsius is", celsius)
     elif temp_choice == 3:
         celsius = float(input("Enter your temperature in Celsius: "))
         kelvin = celsius + 273.15
         print("Kelvin is", kelvin)
     elif temp_choice == 4:
         kelvin = float(input("Enter your temperature in Kelvin: "))
         celsius = kelvin - 273.15
         print("Celsius is", celsius)
     else:
         print("Invalid choice")
 elif choice == 2:
     print(" You chose distance!")
     print("1. Kilometers → Miles")
     print("2. Miles → Kilometers ")
     print("3. Meters → Feet")
     print("4. Feet → Meters")
     dist_choice = input("Enter your choice: ")
     if not dist_choice.isdigit():
         print("Invalid choice! please enter a number")
         continue
     dist_choice = int(dist_choice)

     if dist_choice == 1:
         kilometers = float(input("Enter your distance in Kilometers: "))
         miles = kilometers / 1.609344
         print("Miles is", miles)
     elif dist_choice == 2:
         miles = float(input("Enter your distance in Miles: "))
         kilometers = miles * 1.609344
         print("Kilometers is", kilometers)
     elif dist_choice == 3:
         meters = float(input("Enter your distance in Meters: "))
         feet = meters / 0.3048
         print ("Feet is", feet)
     elif dist_choice == 4:
         feet = float(input("Enter your distance in Feet: "))
         meters = feet * 0.3048
         print ("Meters is", meters)
     else:
         print("Invalid choice")
 elif choice == 3:
     print(" You chose weight!")
     print("1. Kilograms → Pounds ")
     print("2. Pounds → Kilograms ")
     print("3. Grams → Kilograms ")
     print("4. Kilograms → Grams ")
     weight_choice = input("Enter your choice: ")
     if not weight_choice.isdigit():
         print("Invalid choice! please enter a number")
         continue
     weight_choice = int(weight_choice)
     if weight_choice == 1:
         kg=float(input("Enter your weight in Kilograms: "))
         pounds= kg * 2.20462262
         print("Pounds is", pounds)
     elif weight_choice == 2:
         pounds = float(input("Enter your weight in Pounds: "))
         kg = pounds / 2.20462262
         print("Kilograms is", kg)
     elif weight_choice == 3:
         grams= float(input("Enter your weight in Grams: "))
         kg= grams / 1000
         print("Kilograms is", kg)
     elif weight_choice == 4:
         kg= float(input("Enter your weight in Kilograms: "))
         grams = kg * 1000
         print("Grams is", grams)
     else:
         print("Invalid choice")

 elif choice == 4:
     print(" You chose time!")
     print("1. Hours → Minutes ")
     print("2. Minutes → Hours ")
     print("3. Minutes → Seconds")
     print("4. Seconds → Minutes")
     time_choice = input("Enter your choice: ")
     if not time_choice.isdigit():
         print("Invalid choice! please enter a number")
         continue
     time_choice = int(time_choice)
     if time_choice == 1:
         hours = float(input("Enter your time in Hours: "))
         minutes = hours * 60
         print("Minutes is", minutes)
     elif time_choice == 2:
         minutes = float(input("Enter your time in Minutes: "))
         hours = minutes / 60
         print("Hours is", hours)
     elif time_choice == 3:
         minutes = float(input("Enter your time in Minutes: "))
         seconds = minutes * 60
         print("Seconds is", seconds)
     elif time_choice == 4:
         seconds = float(input("Enter your time in seconds: "))
         minutes = seconds / 60
         print("Minutes is", minutes)
     else:
         print("Invalid choice")
 elif choice == 5:
     print(" Exiting the program")
     break
 else:
     print("Invalid choice")











