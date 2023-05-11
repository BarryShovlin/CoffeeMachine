MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "megacoffee": {
        "ingredients": {
            "water": 500,
            "milk": 1000,
            "coffee": 100
        },
        "cost": 10.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(drink):
    if drink == "report" or drink == "off":
        return
    else:
        ingredients = MENU[drink]["ingredients"]
        if ingredients["water"] > resources["water"]:
            print("Sorry, there is not enough water")
        elif ingredients["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
        elif ingredients["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk")
        else:
            print("Sufficient ingredients")


money = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}


def calculate_money(quarters, dimes, nickels, pennies):
    return float((quarters * money["quarter"]) + (dimes * money["dime"]) + (nickels * money["nickel"])\
        + (pennies * money["penny"]))


def make_coffee(coffee):
    ingredients = MENU[coffee]["ingredients"]
    water_loss = ingredients["water"]
    milk_loss = ingredients["milk"]
    coffee_loss = ingredients["coffee"]
    resources["water"] -= water_loss
    resources["milk"] -= milk_loss
    resources["coffee"] -= coffee_loss
    return water_loss, milk_loss, coffee_loss


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    check_resources(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(resources)
    else:
        print("Insert coins")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickels?: "))
        p = int(input("How many pennies?: "))
        total_money_inserted = calculate_money(q, d, n, p)
        if MENU[choice]["cost"] > total_money_inserted:
            print("I'm sorry, that is not enough. Your money is refunded")
        else:
            print("that is enough money")
            resources["money"] += MENU[choice]["cost"]
            if total_money_inserted > MENU[choice]["cost"]:
                change = total_money_inserted - MENU[choice]["cost"]
                print(f"Here is ${change} in change.")
            make_coffee(choice)
            print(f"Here is your {choice}. Enjoy!")


