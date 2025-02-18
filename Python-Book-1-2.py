#!/usr/bin/env python3
"""
Chapter 2: Simple Calculator with Enhanced GUI
-------------------------------------------------
This production-quality application features:
  • A modern GUI for basic arithmetic operations.
  • A class-based design with robust error handling.
  • A dynamically adjusted interface that fits the content.
  • A fixed, high-resolution application icon using 'id01t.jpg'.
      - The icon is loaded via Pillow (PIL) and applied with iconphoto.
  • Clickable links to https://id01t.ca and the GitHub repository.

Ensure that 'id01t.jpg' is in the same folder as this script.
  
Official iD01t Academy example.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import sys

# Import Pillow modules to handle JPEG images
from PIL import Image, ImageTk

class SimpleCalculatorApp:
    def __init__(self, master: tk.Tk) -> None:
        """
        Initialize the application with the main window.
        
        Args:
            master (tk.Tk): The root window instance.
        """
        self.master = master
        self.master.title("Simple Calculator - iD01t Academy")
        self.set_app_icon()
        self.create_widgets()
    
    def set_app_icon(self) -> None:
        """
        Sets a fixed, high-resolution application icon on the title bar and taskbar.
        The icon is loaded from 'id01t.jpg' using Pillow and stored as an instance variable
        to prevent garbage collection.
        """
        try:
            # Open the JPEG image and convert it to a PhotoImage via Pillow.
            image = Image.open("id01t.jpg")
            self.icon = ImageTk.PhotoImage(image)
            self.master.iconphoto(True, self.icon)
        except Exception as e:
            print(f"Warning: App icon not loaded. {e}")
    
    def create_widgets(self) -> None:
        """
        Creates and arranges all the widgets in the application.
        """
        # Main frame with padding to keep content clear of window borders.
        mainframe = ttk.Frame(self.master, padding="20 20 20 20")
        mainframe.grid(row=0, column=0, sticky="NSEW")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        # Title label: a large, bold title for the application.
        title = ttk.Label(mainframe, text="Simple Calculator", font=("Helvetica", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input for the first number.
        ttk.Label(mainframe, text="Enter first number:", font=("Helvetica", 12)) \
            .grid(row=1, column=0, sticky="W", pady=5)
        self.num1_entry = ttk.Entry(mainframe, width=25, font=("Helvetica", 12))
        self.num1_entry.grid(row=1, column=1, sticky="E", pady=5)
        
        # Input for the second number.
        ttk.Label(mainframe, text="Enter second number:", font=("Helvetica", 12)) \
            .grid(row=2, column=0, sticky="W", pady=5)
        self.num2_entry = ttk.Entry(mainframe, width=25, font=("Helvetica", 12))
        self.num2_entry.grid(row=2, column=1, sticky="E", pady=5)
        
        # Dropdown menu for selecting the arithmetic operation.
        ttk.Label(mainframe, text="Select operation:", font=("Helvetica", 12)) \
            .grid(row=3, column=0, sticky="W", pady=5)
        self.operation_var = tk.StringVar(value="Addition")
        operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.operation_menu = ttk.OptionMenu(mainframe, self.operation_var, operations[0], *operations)
        self.operation_menu.config(width=20)
        self.operation_menu.grid(row=3, column=1, sticky="E", pady=5)
        
        # Button to trigger the calculation.
        calc_btn = ttk.Button(mainframe, text="Calculate", command=self.calculate)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Label to display the calculation result.
        self.result_label = ttk.Label(mainframe, text="Result: ", font=("Helvetica", 14, "bold"))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Frame for clickable external links.
        link_frame = ttk.Frame(mainframe)
        link_frame.grid(row=6, column=0, columnspan=2, pady=(30, 0))
        link_style = {"foreground": "blue", "cursor": "hand2", "font": ("Helvetica", 10, "underline")}
        
        # Clickable link for iD01t.ca.
        link_id01t = tk.Label(link_frame, text="Visit iD01t.ca", **link_style)
        link_id01t.pack(side="left", padx=10)
        link_id01t.bind("<Button-1>", lambda e: self.open_url("https://id01t.ca"))
        
        # Clickable link for the GitHub repository.
        link_github = tk.Label(link_frame, text="GitHub Repository", **link_style)
        link_github.pack(side="left", padx=10)
        link_github.bind("<Button-1>", lambda e: self.open_url("https://github.com/iD01t-Softwares/iD01t-Academy"))
    
    def calculate(self) -> None:
        """
        Retrieves user inputs, performs the selected arithmetic operation, 
        and updates the result label with the computed output.
        """
        try:
            # Convert the input strings to floats.
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
            return
        
        # Determine the operation and compute the result.
        operation = self.operation_var.get()
        if operation == "Addition":
            result = num1 + num2
            op_symbol = "+"
        elif operation == "Subtraction":
            result = num1 - num2
            op_symbol = "-"
        elif operation == "Multiplication":
            result = num1 * num2
            op_symbol = "*"
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Math Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
            op_symbol = "/"
        else:
            messagebox.showerror("Operation Error", "Invalid operation selected.")
            return
        
        # Update the result label with the calculated output.
        self.result_label.config(text=f"Result: {num1} {op_symbol} {num2} = {result}")
    
    @staticmethod
    def open_url(url: str) -> None:
        """
        Opens the specified URL in the default web browser.
        
        Args:
            url (str): The URL to open.
        """
        webbrowser.open(url)

def main() -> None:
    """
    Main entry point for the application. Initializes the root window,
    adjusts its size to fit the content, and starts the event loop.
    """
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    
    # Update layout and retrieve the required size based on the content.
    root.update_idletasks()
    required_width = root.winfo_reqwidth()
    required_height = root.winfo_reqheight()
    root.geometry(f"{required_width}x{required_height}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
