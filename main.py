class RecycleSystem:
    # Predefined reward values for each item type
    REWARD_VALUES = {
        'A': 0.10,
        'B': 0.05,
        'C': 0.15
    }
    # Initializes the RecycleSystem object with an empty list of items and a total reward of 0.0
    def __init__(self):
        self.items = []
        self.total_reward = 0.0
    # Adds an item to the system and updates the total reward. If the item type is invalid, it prints an error message
    def add_item(self, item_type):
        if item_type in self.REWARD_VALUES:
            self.items.append(item_type)
            self.total_reward += self.REWARD_VALUES[item_type]
            print(f"Item {item_type} added. Reward: INR{self.REWARD_VALUES[item_type]:.2f}")
        else:
            print(f"Invalid item type: {item_type}. Please enter A, B, or C.")
    # Prints the total reward accumulated so far
    def view_total_reward(self):
        print(f"Total reward accumulated: INR{self.total_reward:.2f}")
    # Resets the system by clearing the list of items and setting the total reward to 0.0
    def reset_system(self):
        self.items = []
        self.total_reward = 0.0
        print("System reset for a new user session.")
# Displays the menu options for the recycle system
def display_menu():
    print("\nRecycle System Menu")
    print("1. Add item")
    print("2. View total reward")
    print("3. Reset system")
    print("4. Exit")
# The main function that runs the recycle system. It creates an instance of RecycleSystem and enters a loop where it displays the menu and processes user input
def main():
    system = RecycleSystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item_type = input("Enter item type (A, B, or C): ").upper()
            system.add_item(item_type)
        elif choice == '2':
            system.view_total_reward()
        elif choice == '3':
            system.reset_system()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
# Ensures that the main function runs only if the script is executed directly, not if it's imported as a module
if __name__ == "__main__":
    main()
