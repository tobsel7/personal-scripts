from math import ceil


def gather_expenses():
    print("Hi, here you can add all the expenses of your group. \n"
          "Finish by entering no value.")
    total_expenses = {}
    while True:
        person = str(input("Enter the name of the person..."))
        if person == "":
            break
        else:
            try:
                expense = float(input("Enter the expense using a . for floating point numbers."))
            except:
                print("Please enter a floating point number without any special characters expect for .")
                continue

            if person in total_expenses:
                total_expenses[person] += expense
            else:
                total_expenses[person] = expense
    return total_expenses


def analyse_expenses(expenses):
    print("\nANALYZING THE EXPENSES OF THE GROUP")
    # calculate total cost and cost of the trip per person
    total = sum(expenses.values())
    cost_per_person = ceil(total / len(expenses) * 100) / 100.0
    print("Total cost: {}".format(total))
    print("Cost per person: {}".format(cost_per_person))

    # calculate balance of each person
    balances = {}
    for name, expense in expenses.items():
        balances[name] = expense - cost_per_person

    print("Balances:")
    print(balances)

    # calculate transfers
    transfers = []
    for name_minus, balance_minus in balances.items():
        if balance_minus < -0.01:
            for name_plus, balance_plus in balances.items():
                if balance_plus > 0:
                    # check if the balance of this person will be corrected after this step
                    # (the rest of the negative balance can be transferred to the person with the positive balance)
                    imbalance_corrected = balance_plus > -balance_minus
                    transfer_amount = ceil((-balance_minus if imbalance_corrected else balance_plus) * 100) / 100.0

                    # update balances
                    balances[name_minus] += transfer_amount
                    balances[name_plus] -= transfer_amount

                    # add transfer to list of transfers
                    transfers.append(
                        {
                            "from": name_minus,
                            "to": name_plus,
                            "amount": transfer_amount
                        }
                    )
                    if imbalance_corrected:
                        # go to next person with negative balance
                        break

    print("Transfers:")
    for transfers in transfers:
        print(transfers)


# entry point for the program
def main():
    analyse_expenses(gather_expenses())


# create point for start of the program and call main()
if __name__ == "__main__":
    main()

