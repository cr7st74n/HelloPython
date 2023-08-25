#  List of classes

classes = []    # Create an empty list to add my classes

NumClasses = True

# Add classes using a while loop
while NumClasses:
    Class = input("Enter one of your Class: ")
    classes.append(Class)
    print(f' I got your Class {Class}')

    moreClasses = input("Do you need more classes ? Yes/No ")
    moreClasses = moreClasses.capitalize()

    # ask the user if he/she needs to add more classes
    if moreClasses.strip() == "Yes":
        print("Got it, keep adding Classes")
    else:
        NumClasses = False
        print("thank you, Here are your Classes !")

# Print the list of Classes
for i in range(0, len(classes)):
    print(f' -{classes[i]} \n')
