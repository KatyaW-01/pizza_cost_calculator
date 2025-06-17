def pizza_size(size):
  if size == "small":
    return 8
  else:
    return 12
  
def delivery(miles):
  if miles <= 5 and miles > 0:
    return 2
  elif miles > 5:
    return 2 + (miles-5) 
  elif miles == 0:
    return 0



customer_pizza_size = input("What size pizza would you like? please enter small or large. ")
customer_toppings = int(input("How many toppings would you like on your pizza? "))
customer_miles = int(input("How many miles away is your house? "))

base_price = pizza_size(customer_pizza_size)
delivery_fee = delivery(customer_miles)

print(delivery_fee)

cost = base_price + customer_toppings + delivery_fee

print(f"Your total cost for your pizza is ${cost}")

