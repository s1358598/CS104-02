# CS 104
# Alexander Metz
# conditions.py

keepGoing = True
count = 0
maxCount = int(input("How many times do you want the program to run? "))

while keepGoing:
    temp = int(input("Please enter the current temperature: "))
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")
    count += 1
    if count >= maxCount:
        break
