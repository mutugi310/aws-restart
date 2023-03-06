userReply = input("Do we need to ship a package? \n (enter yes or no)\n ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

userReply=input("Would you like to buy stamps, buy an envelop, or make a copy?\n (Enter stamps, envelope, or copy.\n ")
if userReply=="stamps":
    print("We have many stam designs to chose from.")
elif userReply=="envelope":
    print("We have may envirope sizes to choose from.")
elif userReply=="copy":
    copies=input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    