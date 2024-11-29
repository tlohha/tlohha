import tkinter as tk

def display_input():
    user_input = entry.get()
    output_label.config(text=f"You entered: {user_input}")

# Create the main application window
app = tk.Tk()
app.title("Simple UI")

# Create an input field
entry_label = tk.Label(app, text="Enter something:")
entry_label.pack(pady=5)

entry = tk.Entry(app, width=30)
entry.pack(pady=5)

# Create a button to trigger the action
submit_button = tk.Button(app, text="Submit", command=display_input)
submit_button.pack(pady=5)

# Label to display the output
output_label = tk.Label(app, text="")
output_label.pack(pady=5)

# Run the application
app.mainloop()
