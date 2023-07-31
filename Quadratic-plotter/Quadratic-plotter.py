import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import webbrowser
from PIL import Image, ImageTk

notebook = None  # Define the notebook variable globally
xy_values_text = None  # Define xy_values_text globally

def plot_quadratic():
    global notebook, xy_values_text  # Access the globally defined notebook and xy_values_text variables
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        min_range = float(entry_min_range.get())
        max_range = float(entry_max_range.get())
        x_interval = float(entry_interval.get())

        # Create a range of x values with user-defined range and interval
        x = np.arange(min_range, max_range + x_interval, x_interval)

        # Calculate y values using the quadratic equation y = ax^2 + bx + c
        y = a * x**2 + b * x + c

        # Calculate the roots using the quadratic formula
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + np.sqrt(discriminant)) / (2*a)
            root2 = (-b - np.sqrt(discriminant)) / (2*a)
            roots = f"Roots: {root1:.2f}, {root2:.2f}"
        elif discriminant == 0:
            root = -b / (2*a)
            roots = f"Root: {root:.2f}"
        else:
            roots = "No real roots"

        # Calculate the x-coordinate of the vertex (maxima/minima)
        vertex_x = -b / (2*a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c

        # Create the plot
        plt.clf()  # Clear the previous plot
        plt.plot(x, y)
        plt.scatter(vertex_x, vertex_y, color='red', label=f"Maxima/Minima: {vertex_x:.2f}, {vertex_y:.2f}")
        plt.title("Quadratic Equation Plot")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.legend()
        plt.text(min_range + (max_range - min_range) * 0.05, np.max(y), roots, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

        # Update the embedded canvas with the new plot
        canvas.draw()

        # Update the values of x and y in the second tab
        xy_values_text.config(state=tk.NORMAL)
        xy_values_text.delete('1.0', tk.END)
        xy_values_text.insert(tk.END, "\n".join([f"{x_val:.2f}, {y_val:.2f}" for x_val, y_val in zip(x, y)]))
        xy_values_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the tkinter GUI
root = tk.Tk()
root.title("Quadratic Equation Plot")

# Set the window icon (replace 'path_to_your_icon.ico' with the actual path to your ICO file)
root.iconbitmap('my.ico')

# Default values for a, b, and c
default_a, default_b, default_c = 2, -2, -4
default_min_range, default_max_range = -10, 10

# Create a Frame for the general information
info_frame = tk.Frame(root)
info_frame.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

# Information about the general form of the quadratic equation
general_label = tk.Label(info_frame, text="General Form: y = ax^2 + bx + c")
general_label.grid(row=0, column=0, padx=5, pady=2)

# Information about the formula to find the roots
roots_label = tk.Label(info_frame, text="Formula for Roots: x = (-b ± √(b^2 - 4ac)) / 2a")
roots_label.grid(row=1, column=0, padx=5, pady=2)

# Information about the formula to find the maxima/minima
max_min_label = tk.Label(info_frame, text="Formula for Maxima/Minima: x = -b / 2a")
max_min_label.grid(row=2, column=0, padx=5, pady=2)

# Create input fields for a, b, and c with default values
entry_a = tk.Entry(root, width=10)
label_a = tk.Label(root, text=" Value of a ")
label_a.grid(row=1, column=0, padx=9, pady=9)
entry_a.insert(0, str(default_a))
entry_a.grid(row=1, column=1, padx=9, pady=9)

entry_b = tk.Entry(root, width=10)
label_b = tk.Label(root, text=" Value of b ")
label_b.grid(row=1, column=2, padx=9, pady=9)
entry_b.insert(0, str(default_b))
entry_b.grid(row=1, column=3, padx=9, pady=9)

entry_c = tk.Entry(root, width=10)
label_b = tk.Label(root, text=" Value of c ")
label_b.grid(row=1, column=4, padx=9, pady=9)
entry_c.insert(0, str(default_c))
entry_c.grid(row=1, column=5, padx=9, pady=9)

# Create input fields for the min and max range of x
label_min_range = tk.Label(root, text="Min Range")
label_min_range.grid(row=2, column=0, padx=9, pady=9)
entry_min_range = tk.Entry(root, width=10)
entry_min_range.insert(0, str(default_min_range))
entry_min_range.grid(row=2, column=1, padx=9, pady=9)

label_max_range = tk.Label(root, text="Max Range")
label_max_range.grid(row=2, column=2, padx=9, pady=9)
entry_max_range = tk.Entry(root, width=10)
entry_max_range.insert(0, str(default_max_range))
entry_max_range.grid(row=2, column=3, padx=9, pady=9)

# Create input fields for the interval of x
label_interval = tk.Label(root, text="Insert Interval ")
label_interval.grid(row=2, column=4, padx=9, pady=9)
entry_interval = tk.Entry(root, width=10)
entry_interval.insert(0, "1")  # Default interval value
entry_interval.grid(row=2, column=5, padx=9, pady=9)

# Create a button to plot the quadratic equation
plot_button = tk.Button(root, text="Plot", command=plot_quadratic)
plot_button.grid(row=2, column=6, padx=9, pady=9)

# Create a Frame for the NavigationToolbar2Tk
toolbar_frame = tk.Frame(root)
toolbar_frame.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

# Create a ttk Notebook for tabbed interface
notebook = ttk.Notebook(root)
notebook.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

# First Tab - Matplotlib plot with NavigationToolbar
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Quadratic Plot")

# Create a Figure and a Canvas for matplotlib plot with default values
fig = plt.figure(figsize=(7, 5))
canvas = FigureCanvasTkAgg(fig, master=tab1)
canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)

# Add a NavigationToolbar2Tk to enable zooming and panning
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
toolbar.grid(row=0, column=0)  # Use grid for the toolbar in its parent frame

# Second Tab - Values of x and y
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Values of x and y")

xy_values_text = tk.Text(tab2, width=40, height=30, state=tk.DISABLED)
xy_values_text.grid(row=0, column=0, padx=10, pady=10)

# Add a Scrollbar to the Text widget
scrollbar = tk.Scrollbar(tab2, command=xy_values_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
xy_values_text.config(yscrollcommand=scrollbar.set)

# Plot the default quadratic equation
plot_quadratic()

# Third Tab - Author Information
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="  Author  ")

# Load author photo
author_photo_path = "shahino.jpg"
author_image = Image.open(author_photo_path)
author_photo = ImageTk.PhotoImage(author_image)

# Display author photo
author_photo_label = tk.Label(tab3, image=author_photo)
author_photo_label.grid(row=0, column=0, padx=10, pady=10)

# Display author name
author_name_label = tk.Label(tab3, text="Shahino Mah Abdullah", font=("Helvetica", 12, "bold"))
author_name_label.grid(row=1, column=0, padx=10, pady=2)

# Display author web address
author_web_label = tk.Label(tab3, text="github.com/shahinomah", cursor="hand2", fg="blue", font=("Helvetica", 10))
author_web_label.grid(row=2, column=0, padx=10, pady=2)

# Function to open the link when the label is clicked
def open_github(event):
    webbrowser.open("https://github.com/shahinomah")

# Bind the label to the function to open the link
author_web_label.bind("<Button-1>", open_github)

# Add a note at the bottom of the tkinter window
note_label = tk.Label(root, text="Shahino Mah (2023)", cursor="hand2", fg="black", font=("Helvetica", 10))
note_label.grid(row=5, column=0, columnspan=6, pady=5)

# Function to open the link when the label is clicked
def open_github(event):
    webbrowser.open("https://github.com/shahinomah")

# Bind the label to the function to open the link
note_label.bind("<Button-1>", open_github)

root.mainloop()
