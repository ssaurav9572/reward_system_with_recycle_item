Run the Script: Open a terminal or command prompt, navigate to the directory where recycle_system.py is saved, and run the script using the command
Assumptions and Design Decisions

    Predefined Reward Values: The reward values for each item type (A, B, C) are predefined and stored in a class-level dictionary REWARD_VALUES. This makes it easy to update reward values if needed.
    Item Types Validation: The add_item method validates the item type against the predefined reward values. If an invalid item type is entered, an error message is printed.
    User Interaction: The system interacts with the user via the console, allowing them to add items, view total rewards, reset the system, or exit.
    Case Insensitivity: Item types entered by the user are converted to uppercase to ensure case insensitivity.
    Simple Menu Navigation: The menu is designed to be simple and intuitive, guiding the user through the available options.
