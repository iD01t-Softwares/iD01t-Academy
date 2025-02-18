#!/usr/bin/env python3
"""
iD01t Academy Project Examples CLI Interface
---------------------------------------------
This script consolidates multiple iD01t Academy project examples into a single,
menu-driven command-line interface (CLI). Each example corresponds to a chapter
in the iD01t Academy Python Exercises series and is implemented as its own function.

Available Examples:
  1. Chapter 1: Hello, World and Basic I/O
  2. Chapter 2: Simple Calculator
  3. Chapter 3: Guess the Number Game
  4. Chapter 4: To-Do List CLI App
  5. Chapter 5: Rock, Paper, Scissors Game
  6. Chapter 6: Simple Contact Manager

Usage:
  Run the script using Python:
      python id01t_academy_projects_cli.py
  Then, follow the on-screen instructions to select and run a project example.
"""

def chapter1_hello_world() -> None:
    """
    Chapter 1: Hello, World and Basic I/O
    ---------------------------------------
    This function prints "Hello, World!", prompts the user for their name,
    and then greets them using an f-string.
    
    Steps:
      1. Display a welcome message.
      2. Prompt the user for their name.
      3. Print a personalized greeting.
    """
    print("\n--- Chapter 1: Hello, World and Basic I/O ---")
    print("Hello, World!")
    name: str = input("What's your name? ")
    print(f"Hello, {name}!")


def chapter2_simple_calculator() -> None:
    """
    Chapter 2: Simple Calculator
    ----------------------------
    This function prompts the user to enter two numbers and choose an arithmetic
    operation (Addition, Subtraction, Multiplication, or Division). It then performs
    the selected calculation and displays the result.
    
    Steps:
      1. Prompt for two numeric inputs.
      2. Display a menu for selecting an operation.
      3. Perform the operation with proper error checking (including division by zero).
      4. Print the result.
    """
    print("\n--- Chapter 2: Simple Calculator ---")
    print("Welcome to the Simple Calculator!")
    try:
        num1: float = float(input("Enter the first number: "))
        num2: float = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter your choice (1/2/3/4): ").strip()

    if operation == '1':
        result = num1 + num2
        op_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        op_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        op_symbol = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
        op_symbol = '/'
    else:
        print("Invalid operation selected.")
        return

    print(f"\nResult: {num1} {op_symbol} {num2} = {result}")


def chapter3_guess_the_number() -> None:
    """
    Chapter 3: Guess the Number Game
    --------------------------------
    This function implements a classic guessing game where the computer randomly
    selects a number between 1 and 100. The user is prompted to guess the number,
    and after each guess, feedback is provided until the correct number is guessed.
    
    Steps:
      1. Generate a random target number.
      2. Continuously prompt the user for guesses.
      3. Provide hints ("Too low" or "Too high") until the guess is correct.
      4. Display the total number of attempts.
    """
    import random
    print("\n--- Chapter 3: Guess the Number Game ---")
    target: int = random.randint(1, 100)
    attempts: int = 0
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess: int = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1
        
        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


def chapter4_todo_list_app() -> None:
    """
    Chapter 4: To-Do List CLI App
    -----------------------------
    This function implements a menu-driven CLI for managing a to-do list.
    Users can add tasks, view the list of tasks, or remove tasks interactively.
    
    Steps:
      1. Display a menu of options (add, view, remove, or exit).
      2. Handle each operation based on user selection.
      3. Maintain and update a list of tasks.
    """
    print("\n--- Chapter 4: To-Do List CLI App ---")
    tasks: list[str] = []
    
    while True:
        print("\n=== To-Do List App ===")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            task = input("Enter a new task: ").strip()
            tasks.append(task)
            print("Task added!")
        elif choice == '2':
            if tasks:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks available.")
        elif choice == '3':
            if tasks:
                print("Select a task to remove:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    index_to_remove: int = int(input("Enter task number to remove: ").strip()) - 1
                    if 0 <= index_to_remove < len(tasks):
                        removed_task = tasks.pop(index_to_remove)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No tasks to remove.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def chapter5_rock_paper_scissors() -> None:
    """
    Chapter 5: Rock, Paper, Scissors Game
    -------------------------------------
    This function lets the user play Rock, Paper, Scissors against the computer.
    The computer's move is chosen at random, and the game continues until the user
    types 'exit'.
    
    Steps:
      1. Prompt the user for their move.
      2. Randomly select the computer's move.
      3. Compare moves to determine the winner.
      4. Continue until the user types 'exit'.
    """
    import random
    print("\n--- Chapter 5: Rock, Paper, Scissors Game ---")
    moves = ['rock', 'paper', 'scissors']
    
    while True:
        user_move = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").strip().lower()
        if user_move == 'exit':
            print("Thanks for playing!")
            break
        if user_move not in moves:
            print("Invalid move. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")
        
        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == 'rock' and computer_move == 'scissors') or \
             (user_move == 'paper' and computer_move == 'rock') or \
             (user_move == 'scissors' and computer_move == 'paper'):
            print("You win!")
        else:
            print("You lose!")


def chapter6_contact_manager() -> None:
    """
    Chapter 6: Simple Contact Manager
    ---------------------------------
    This function implements a simple contact management system via a CLI.
    Users can add contacts, view all contacts, search for a contact, or delete a contact.
    
    Steps:
      1. Display a menu for contact management.
      2. Handle adding, viewing, searching, and deleting contacts.
      3. Store contacts in a dictionary.
    """
    print("\n--- Chapter 6: Simple Contact Manager ---")
    contacts: dict[str, str] = {}
    
    while True:
        print("\n=== Contact Manager ===")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete a contact")
        print("5. Return to main menu")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone number: ").strip()
            contacts[name] = phone
            print("Contact added!")
        elif choice == '2':
            if contacts:
                print("\nContacts:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts available.")
        elif choice == '3':
            search_name = input("Enter the name to search: ").strip()
            if search_name in contacts:
                print(f"{search_name}: {contacts[search_name]}")
            else:
                print("Contact not found.")
        elif choice == '4':
            delete_name = input("Enter the name of the contact to delete: ").strip()
            if delete_name in contacts:
                del contacts[delete_name]
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def display_main_menu() -> None:
    """
    Displays the main menu for the iD01t Academy Python Project Book 1 Examples.
    """
    print("\n==========================================")
    print("    iD01t Academy Project Examples CLI")
    print("==========================================")
    print("1. Chapter 1: Hello, World and Basic I/O")
    print("2. Chapter 2: Simple Calculator")
    print("3. Chapter 3: Guess the Number Game")
    print("4. Chapter 4: To-Do List CLI App")
    print("5. Chapter 5: Rock, Paper, Scissors Game")
    print("6. Chapter 6: Simple Contact Manager")
    print("7. Exit")


def main() -> None:
    """
    Main entry point for the iD01t Academy Project Examples CLI Interface.
    
    Continuously displays the main menu and prompts the user to select an example to run,
    until the user chooses to exit.
    """
    while True:
        display_main_menu()
        choice = input("Select an example to run (1-7): ").strip()
        if choice == '1':
            chapter1_hello_world()
        elif choice == '2':
            chapter2_simple_calculator()
        elif choice == '3':
            chapter3_guess_the_number()
        elif choice == '4':
            chapter4_todo_list_app()
        elif choice == '5':
            chapter5_rock_paper_scissors()
        elif choice == '6':
            chapter6_contact_manager()
        elif choice == '7':
            print("Exiting iD01t Academy Project Examples. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
