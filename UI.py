import tkinter as tk
from query import main

def search():
    query = query_entry.get()
    result = main(query)
    # You can display the search results in a separate window or widget.
    # For simplicity, let's print the results in the console.
    print(result)

# Create the main window
window = tk.Tk()
window.title("News Search Engine")

# Create a label for the query input
query_label = tk.Label(window, text="Enter your query:")
query_label.pack()

# Create an entry field for the user to input their query
query_entry = tk.Entry(window)
query_entry.pack()

# Create a search button to trigger the query
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()

# Run the Tkinter main loop
window.mainloop()
