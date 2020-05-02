#Define our list of users
users = ["ben", "steve", "john"]
print("Welcome to the Shipping Accounts Program")

#Get user input
username = input("\nHello, what is your username: ").lower().strip()

#Our user is in our list...
if username in users:
  #print prices
  print("\nHello " + username + ". Welcome back to your account.")
  print("Current shipping prices are as follows:")
  print("\nShipping orders 0 to 100: \t\t€5.10 each")
  print("Shipping orders 100 to 500: \t€5.00 each")
  print("Shipping orders 500 to 1000: \t€4.95 each")
  print("Shipping orders over 1000: \t\t€4.80 each")

  #determine price
  quantity = (int(input("\nHow many items would you like to ship: ")))
  if quantity < 100:
      cost = 5.10
  elif quantity < 500:
      cost = 5.00
  elif quantity < 1000:
      cost = 4.95
  else:
      cost = 4.80
  
  #Display
  bill = quantity*cost
  bill = round(bill, 2)
  print("To ship " + str(quantity) + " items it will cost you €" + str(bill) + " at €" + str(cost) + " per item.")

  #Place the order
  choice = input("\nWould you like to place the order (y/n): ").lower()
  if choice.startswith("y"):
    print("Okay. Shipping your " + str(quantity) + " items")
    print("Thank you for placing an order today, goodbye")
  else:
      print("Okay, no order is being placed at this time.")

#No username
else:
  print("\nSorry, you do not have an account with us.")
  print("Goodbye")