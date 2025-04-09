import os
from helper_funcs.helper import menu_select


def run_coin_program():




    # Function for calculating the coin change amount
    def coin_change(coins, amount):
        if amount <= 0:
            return (0, [])
    
        coin_count = 0
        coin_used = []
    
        for name, value in coins:
            while amount >= value:
                amount = round(amount - value, 2)  # Round to avoid floating-point issues
                coin_count += 1
                coin_used.append(name)
        return (coin_count, coin_used)





    # Function for loading coin denominations
    def load_coin_denominations(country):
        filename = os.path.join("coin_change", f"{country.lower()}_denominations.txt")

        coins = []
        with open(filename) as file:
            for line in file:
                try:
                    name, value = line.strip().split('-')
                    coins.append((name, int(value)))  # Denominations are in pennies (integer)
                except ValueError:
                    raise ValueError("Invalid coin format in file. Expected 'Name-Value' format.")

        # Manual sorting by value in descending order
        coins.sort(key=lambda x: x[1], reverse=True)
        return coins





    # Handles the user interaction and calls required functions
    countries = ["USA", "UK", "Canada", "EU", "Mexico"]
    selection = menu_select("Select a country for coin denominations", *countries)
    country = countries[selection - 1]

    coins = load_coin_denominations(country)
    while True:
        try:
            amount = float(input("Enter target amount: "))
            if amount > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Convert the amount to pennies (multiply by 100)
    amount_in_pennies = round(amount * 100)  # Convert to integer pennies

    num_coins, coin_names = coin_change(coins, amount_in_pennies)
    print(f"Minimum number of denominations needed: {num_coins}")
    print("Denominations used:", ", ".join(coin_names))

