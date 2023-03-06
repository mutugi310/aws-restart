correctName="Joe"
name=input("Who are you? ")
while name != correctName:
    name=input("Who are you? ")
if name== correctName:
    password=input("Hello, Joe. \n What is the Password? (it is a fish.)")
if password=="swordfish":
    print("Acess granted.")
elif password!="swordfish":
    password=input("Please reenter the correct password!!")


else:
    print("wrong password!")