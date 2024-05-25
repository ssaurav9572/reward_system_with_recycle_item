# reward_system_with_recycle_item
Explanation:

    Item Acceptance:
        The RecycleSystem class contains a dictionary REWARD_VALUES that defines the reward for each type of item.
        The add_item method checks if the item type is valid, adds it to the list of items, and updates the total reward.

    User Interface:
        The CLI is implemented in the main function, displaying a menu and handling user inputs.
        Users can add items, view total rewards, and reset the system.

    Data Management:
        The RecycleSystem class maintains a record of accepted items and the total reward.
        The reset_system method clears the record for a new user session.

    Code Quality:
        The code is clean, readable, and well-documented with appropriate class and method usage.
        Error handling is implemented for invalid item types and menu choices.

This project can be run as a standalone Python script, providing an interactive command-line interface for users to simulate the collection and rewarding of recyclable items.
