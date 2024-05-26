Run the Script: Open a terminal or command prompt, navigate to the directory where main.py is saved, and run the script using the command

Overview of the Code Structure
The code is structured into several components to handle the recycling system's functionalities. Here's a breakdown of the structure:

    Class Definition: RecycleSystem
        Attributes:
            REWARD_VALUES: A class attribute (dictionary) that defines the reward value for each item type.
            items: An instance attribute (list) that stores the types of items added to the system.
            total_reward: An instance attribute (float) that keeps track of the total reward accumulated.
        Methods:
            __init__(): Initializes the instance attributes.
            add_item(item_type): Adds an item to the system, updates the total reward, and prints a message indicating the item added and its reward. Validates the item type.
            view_total_reward(): Prints the total reward accumulated so far.
            reset_system(): Resets the system by clearing the list of items and setting the total reward to 0.0, and prints a message indicating the reset.

    Function Definition: display_menu
        Purpose: Displays the menu options to the user.

    Function Definition: main
        Purpose: Contains the main logic for running the recycling system, including:
            Creating an instance of RecycleSystem.
            Displaying the menu and processing user input in a loop until the user chooses to exit.
            Handling different choices: adding an item, viewing total reward, resetting the system, and exiting the program.

    Entry Point Check
        Purpose: Ensures that the main function runs only if the script is executed directly, not if it's imported as a module.
        Code: if __name__ == "__main__": main()

Assumptions and Design Decisions

    Predefined Reward Values: The reward values for each item type (A, B, C) are predefined and stored in a class-level dictionary REWARD_VALUES. This makes it easy to update reward values if needed.
    Item Types Validation: The add_item method validates the item type against the predefined reward values. If an invalid item type is entered, an error message is printed.
    User Interaction: The system interacts with the user via the console, allowing them to add items, view total rewards, reset the system, or exit.
    Case Insensitivity: Item types entered by the user are converted to uppercase to ensure case insensitivity.
    Simple Menu Navigation: The menu is designed to be simple and intuitive, guiding the user through the available options.
