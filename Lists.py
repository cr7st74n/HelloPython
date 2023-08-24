#  List of classes

classes = []    # Create an empty list to add my classes

NumClasses = True

while NumClasses:
    Class = input("Enter one of your Class: ")
    classes.append(Class)
    print(f' I got your Class {Class}')
    # ask the user if he/she needs to add more classes
    moreClasses = input("Do you need more classes ?")
    if moreClasses == "Yes":
        print("Got it, keep adding Classes")
    else:
        NumClasses = False
        print("thank you, Here are your Classes !")

for i in range(0, len(classes)):
    print(f' - {classes[i]} \n')
