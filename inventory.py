#define class named shoe with country, code, product, cost and quantity
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return (
            f"Country: {self.country}\n"
            f"Code: {self.code}\n"
            f"Product: {self.product}\n"
            f"Cost: R{self.cost:.2f}\n"
            f"Quantity: {self.quantity}"
        )   

#open list to be used to store a list of objects of shoes
shoes_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            #skip the first line heading
            next(file)
            for line in file:
                data = line.strip().split(",")

                shoe = Shoe(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4]
                )

                shoes_list.append(shoe)

    except FileNotFoundError:
        print("Inventory file not found.")

    except Exception as error:
        print(error)

#to capture a new shoe
def capture_shoes():

    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)

    shoes_list.append(shoe)

    print("Shoe added successfully.")

#to view all shoes in txt file
def view_all():
    for shoe in shoes_list:
        print("-------------------------")
        print(shoe)

#to find the smallest quantity to restock
def re_stock():
    lowest = min(shoes_list, key=lambda shoe: shoe.quantity)

    print(lowest)

    choice = input("Restock this item? (yes/no): ").lower()

    if choice == "yes":

        amount = int(input("How many would you like to add? "))

        lowest.quantity += amount

        print("Stock updated.")
#create update function hearafter
        update_inventory_file()

def update_inventory_file():

    with open("inventory.txt", "w") as file:

        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoes_list:

            file.write(
                f"{shoe.country},"
                f"{shoe.code},"
                f"{shoe.product},"
                f"{shoe.cost},"
                f"{shoe.quantity}\n"
            )

#to search for shoe in inventory
def search_shoe():

    code = input("Enter shoe code: ")

    for shoe in shoes_list:

        if shoe.code == code:

            print(shoe)
            return

    print("Shoe not found.")
#to calculate the value per item where formulae is value = cost * quantity
def value_per_item():

    for shoe in shoes_list:

        value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"{shoe.product}: R{value:.2f}"
        )

#code to determine product with the highest wuatity and print shoe as being for sale
def highest_qty():

    highest = max(shoes_list, key=lambda shoe: shoe.quantity)

    print("FOR SALE!")

    print(highest)

#a menu that executes each function
read_shoes_data()
while True:

    print("\n========== NIKE INVENTORY ==========")
    print("Please select the relevant inventory option")
    print("1. View all shoes")
    print("2. Add shoe")
    print("3. Restock")
    print("4. Search shoe")
    print("5. Total Value for each item")
    print("6. Highest quantity stock")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
