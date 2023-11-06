items = {}
order = {}
total_bill = 0
total_coupons = 0

while True:
    print("Choose an option:")
    print("1. Start a new order")
    print("2. Close the program")
    choice = int(input())

    if choice == 2:
        print("bye bye")
        break
    elif choice == 1:
        while True:
            print("Options:")
            print("1. Add a new item")
            print("2. Check the total of the bill")
            print("3. Add a coupon")
            print("4. Checkout")
            option = int(input())

            if option == 1:
                item_name = input("Enter item name: ")
                item_price = float(input("Enter item price: "))
                items[item_name] = item_price
                order[item_name] = order.get(item_name, 0) + 1
                print("Item added to the order.")
            elif option == 2:
                print(f"The total of your bill is: {total_bill}")
            elif option == 3:
                coupon_value = float(input("Enter coupon value: "))
                total_coupons += coupon_value
                print("Coupon added.")
            elif option == 4:
                print("Items bought and their quantities:")
                for item_name, quantity in order.items():
                    item_price = items[item_name]
                    item_total = quantity * item_price
                    total_bill += item_total
                    print(f"{item_name} x{quantity}: ${item_total}")

                print(f"Total of the order: ${total_bill}")
                print(f"Total of coupons: ${total_coupons}")
                total_to_pay = total_bill - total_coupons
                print(f"Total to pay: ${total_to_pay}")

                
                
