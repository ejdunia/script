# a program that gets user input (shopping items and their prices), 
# gives discount if a condition is reached and prints the items and prices

def get_receipt(receipt):
    """passes a dictionary as an argument, loops through it
    then prints out the total and the list of stuff bought"""
    print("\nThe goods bought and their prices are: ")
    for items, prices in receipt.items():
        print(f"{items}: {prices}")


def get_discount(receipt):
    """ checks the total price and gives a discount if available """
    prices_list = receipt.values()
    total_price = sum(prices_list)
    print(f"The total price is: {total_price}")
    if total_price > 10000:
        print(f"You have earned a 5% discount for your purchase of above N10,000,"
              f"\nYour new total is {total_price - (total_price * .05)}")
    elif total_price > 7000:
        print(f"You have earned a 2% discount for your purchase of above N7,000,"
              f"\nYour new total is {total_price - (total_price * .02)}")
    else:
        print(f" your total is {total_price}, hence you don't qualify for a discount.\n...Shop more perhaps")


user_items = {}
        
print("\nEnter the name of an item and the price\n"
          "You can enter 'end' to stop the program.\n"
          "Input only numbers for the prices\n"
          "")


while True:
    item = input('Enter an item: ').strip()
    if item.lower() == 'end':
        break
    try:
        price = float(input('Enter its price N:'))
    except ValueError:
        print("you did not enter a number!!! start again and follow instructions")
        continue
    else:
        user_items[item] = price
    
get_receipt(user_items)
get_discount(user_items)
