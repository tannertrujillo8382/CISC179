import tkinter as tk
from tkinter import messagebox

class MPGCalculator:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Gas Mileage Calculator")

        # Gallons input
        tk.Label(self.main_window, text="Gallons of gas:").grid(row=0, column=0)
        self.gallons_entry = tk.Entry(self.main_window)
        self.gallons_entry.grid(row=0, column=1)

        # Miles input
        tk.Label(self.main_window, text="Miles per tank:").grid(row=1, column=0)
        self.miles_entry = tk.Entry(self.main_window)
        self.miles_entry.grid(row=1, column=1)

        # Result label
        self.result_label = tk.Label(self.main_window, text="MPG: ")
        self.result_label.grid(row=3, column=0, columnspan=2)

        # Calculate button
        tk.Button(self.main_window, text="Calculate MPG", command=self.calculate_mpg).grid(row=2, column=0, columnspan=2)

        tk.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())

            mpg = miles / gallons

            self.result_label.config(text=f"MPG: {mpg:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Gallons cannot be zero.")

# Run the program
MPGCalculator()
