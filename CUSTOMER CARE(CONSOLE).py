'''a="logincode"
b="password"
logincode="shawlzfashion815"
password="09876"
c=input("Enter your name: ")
d=input("Enter logincode: ")
e=input("Enter password: ")

if d==a and e==b:
    print("welcome",c)'''
c="sales"
print("Welcome to our service\nThis is shawlz fashion house\nWe sell all types of fashion brands and wears\n")
print("Here is the list of our brands:\nBrand1=Louisvuitton\nBrand2=Versace\nBrand3=Hermes\nBrand4=Dior\nBrand5=Gucci\n")
print("Here are the options of wears:\nOption1=Dinner Gown\nOption2=Suit\nOption3=Tops\nOption4=Skirt\nOption5=Trouser ")
a=input("Which brand do you wish to purchase?: \n")
b=input("Choose the option of wears that you want:\n")
c=int(input("Enter sales amount :"))
discount=int(input("Enter discount percentage :"))
output=c * (discount / 100)
print("The sum up of your bill is: ", output)

