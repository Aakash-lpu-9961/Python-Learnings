# Health Management System Project in Python

import time


def getdate():
    import datetime
    return datetime.datetime.now()



print("-------------------------------------------------------------------------------")
print("\t\t\t WELCOME \t TO \t HEALTH \tMANAGEMENT \t SYSTEM")
print("--------------------------------------------------------------------------------")
print("\t\t\t\t\t\t [1] Log the Record\n")
print("\t\t\t\t\t\t [2] Retrieve the Data\n")

choice = int(input("\t\tPress your desired choice:-"))
print("\n")

if choice >2:
    print("Invalid Entry")
    exit()
elif choice <1:
    print("Check you entry")
    exit()

print("\t\t\t\t\t\tOKAY!!! WAIT DATA PROCESSING")
# time.sleep(1.5)
print("--------------------------------------------------------------------------------")

print("\t\t\t CHOOSE THE CANDIDATE  \n")
print("\t\t\t\t\t\t\t [1] Aakash Kumar \n \t\t\t\t\t\t\t [2] Sagar Kumar \n \t\t\t\t\t\t\t [3] Kumar Radha")
print("\n")
choice1 = int(input("\t\tPress your desired choice:-"))
print("\n")

if choice1 <1:
    print("Invalid Entry")
    exit()
elif choice1 >3:
    print("Check your entry")
    exit()

print("\t\t\t\t\t\tOKAY!!! WAIT DATA PROCESSING")
# time.sleep(1.5)
print("--------------------------------------------------------------------------------")

if choice1==1:
    print("\t\t\t\t\t\t\t  CHOOSE WHAT YOU WANT TO DO")
    time.sleep(2)
    print("\t\t\t\t\t\t [1] Enter Diet")
    print("\t\t\t\t\t\t [2] Enter Exercise")
    print("\n")
    choice3 = int(input("\t\tPress your desired choice:-"))
    if choice3==1:
        a = open("aakashdiet.txt", "a")
        a.write("\n")
        a.write(str(getdate()))
        a.write("\t\t-->")
        b = a.write(input("Write your routine of exercise and diet along with date:\n"))


    elif choice3==2:
        c = open("aakashexercise.txt", "a")
        c.write("\n")
        c.write(str(getdate()))
        c.write("\t\t-->")
        d = c.write(input("Write your routine of exercise and diet along with date:\n"))




elif choice1==2:
    print("\t\t\t\t\t\t\t CHOOSE WHAT YOU WANT TO DO")
    time.sleep(2)
    print("\t\t\t\t\t\t [1] Enter Diet")
    print("\t\t\t\t\t\t [2] Enter Exercise")
    print("\n")
    choice3 = int(input("\t\tPress your desired choice:-"))
    if choice3 == 1:
        e = open("sagardiet.txt", "a")
        e.write("\n")
        e.write(str(getdate()))
        e.write("\t\t-->")
        f =e.write(input("Write your routine of exercise and diet along with date:\n"))


    elif choice3 == 2:
        g = open("sagarexercise.txt", "a")
        g.write("\n")
        g.write(str(getdate()))
        g.write("\t\t-->")
        h = g.write(input("Write your routine of exercise and diet along with date:\n"))




elif choice1==3:
    print("\t\t\t\t\t\t\t  CHOOSE WHAT YOU WANT TO DO")
    time.sleep(2)
    print("\t\t\t\t\t\t [1] Enter Diet")
    print("\t\t\t\t\t\t [2] Enter Exercise")
    print("\n")
    choice3 = int(input("\t\tPress your desired choice:-"))
    if choice3 == 1:
        i = open("radhadiet.txt", "a")
        i.write("\n")
        i.write(str(getdate()))
        i.write("\t\t-->")
        j = i.write(input("Write your routine of exercise and diet along with date:\n"))


    elif choice3 == 2:
        k = open("radhaexercise.txt", "a")
        k.write("\n")
        k.write(str(getdate()))
        k.write("\t\t-->")
        l= k.write(input("Write your routine of exercise and diet along with date:\n"))








print()

# print("\n")
# print("\t\t\t\t\t\tOKAY!!! WAIT DATA PROCESSING")
# time.sleep(3)
# print("--------------------------------------------------------------------------------")



print(getdate())

"""if choice==1:
    f = open("Learning3.txt", "r+")
    d = f.write(input("Write your routine of exercise and diet along with date:\n"))
"""