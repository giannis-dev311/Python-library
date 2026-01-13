print("*                                                                                    *")
print("*                                                                                    *")
print("*                                                                                    *")
print("*           WELCOME TO THE THEATRE                                                   *")
print("*                                                                                    *")
print("*                                                                                    *")
print("*                                                                                    *")

age = int(input("Enter your age: "))
price = 10.00

if age >= 65:
    print("You are a senior citizen")
    final_price = price * 0.75
elif age >= 18:
    print("You are an adult")
    final_price = price
else:
    print("You are a child")
    final_price = price * 0.5

print(f"Ticket price: ${final_price}")

has_ticket = input("Do you have a ticket? (yes/no): ").lower()

if has_ticket == "yes":
    print("You may enter ")
else:
    want_ticket = input("Do you want to buy a ticket? (yes/no): ").lower()
    
    if want_ticket == "yes":
        print(f"Please pay ${final_price} and enjoy the show ")
    else:
        print("No ticket, no entry. Have a nice day ")
