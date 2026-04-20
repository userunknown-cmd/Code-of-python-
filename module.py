payments = {}

while True:
    print("\n1. Add Payment")
    print("2. View Payments")
    print("3. Total Pending")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter person's name: ")
        amount = int(input("Enter amount: "))
        
        if name in payments:
            payments[name] += amount
        else:
            payments[name] = amount

        print("Payment added!")

    elif choice == "2":
        if not payments:
            print("No pending payments.")
        else:
            for name, amount in payments.items():
                print(name, "->", amount)

    elif choice == "3":
        total = sum(payments.values())
        print("Total pending amount:", total)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")