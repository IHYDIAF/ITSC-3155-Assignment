import data
import sandwich_maker
import cashier

def main():
    resources = data.resources
    recipes = data.recipes
    sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
    cashier_instance = cashier.Cashier()

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            print("Current resources:")
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item}: {amount}")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print(f"Cost: ${sandwich['cost']:.2f}")
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
                    print(f"Here is your {choice} sandwich. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid input. Please choose again.")

if __name__ == "__main__":
    main()