class Check:
    def __init__(self):
        self.n = []

    def add(self, a):
        self.n.append(a)

    def remove(self, b):
        if b in self.n:
            self.n.remove(b)
        else:
            print("Element not found in the list.")

    def dis(self):
        return self.n

obj = Check()
choice = -1

while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        n = int(input("Enter number to append: "))
        obj.add(n)
        print("List:", obj.dis())
    elif choice == 2:
        n = int(input("Enter number to remove: "))
        obj.remove(n)
        print("List:", obj.dis())
    elif choice == 3:
        print("List:", obj.dis())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
    print()