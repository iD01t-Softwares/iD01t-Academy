#!/usr/bin/env python3
"""
Chapter 1: Hello, World! and Basic Input/Output
-------------------------------------------------
This script demonstrates basic Python I/O operations including:
  • Displaying a welcome message.
  • Reading user input.
  • Using f-strings to personalize output.

Official iD01t Academy example.
"""

def greet_user() -> None:
    """
    Prompts the user for their name and prints a personalized greeting.
    
    Steps:
      1. Prints a welcome message ("Hello, World!").
      2. Asks the user to enter their name.
      3. Greets the user using their provided name.
    """
    # Step 1: Print a welcome message to the console.
    print("Hello, World!")
    
    # Step 2: Prompt the user to enter their name.
    # The input() function reads a line of text from the user.
    name: str = input("What's your name? ")
    
    # Step 3: Greet the user with a personalized message.
    # f-strings allow us to embed the variable 'name' directly in the string.
    print(f"Hello, {name}!")

def main() -> None:
    """
    Main entry point of the program.
    
    The main() function serves as the starting point of the script, 
    calling greet_user() to execute the core functionality.
    """
    greet_user()

if __name__ == "__main__":
    # This ensures the script runs only when executed directly,
    # and not when imported as a module in another script.
    main()
