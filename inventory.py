class Inventory:
    def _init_(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Item '{name}' updated. Current quantity: {self.items[name]}")

    def get_item(self, name):
        if name in self.items:
            print(f"Item: {name}, Quantity: {self.items[name]}")
        else:
            print(f"Item '{name}' not found in inventory.")

    def total_quantity(self):
        total = sum(self.items.values())
        print(f"Total quantity of all items: {total}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory System Menu:")
        print("1. Add/Update Item")
        print("2. Retrieve Item Information")
        print("3. Display Total Quantity")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)

        elif choice == '2':
            name = input("Enter item name to retrieve: ")
            inventory.get_item(name)

        elif choice == '3':
            inventory.total_quantity()

        elif choice == '4':
            print("Exiting Inventory System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()