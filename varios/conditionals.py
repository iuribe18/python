# print("Wlcome to the RollerCoaster")
# height = int(input("What is your Height in cm: ? "))
# if height >= 120:
#     print("You can ride")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Child Tickets are $5")
#     elif age <=18:
#         print("Youth Tickets are $7")
#     else:
#         print("Adult Tickets are $12")
# else:
#     print("You need to be taller")
#
print("Wlcome to the RollerCoaster")
height = int(input("What is your Height in cm: ? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5")
    elif age <=18:
        bill = 5
        print("Youth Tickets are $7")
    elif age >=45 and age <=55:
        bill = 0
        print("Tickets are for Free")
    else:
        bill = 12
        print("Adult Tickets are $12")
    photo = input("Do you want a Photo taken (Y/N): ")
    if photo == "y":
        bill += 3
    print("Total $ " + str(bill))
else:
    print("You need to be taller")