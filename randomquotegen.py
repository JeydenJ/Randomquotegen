import tkinter as tk
import requests

def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    if len(data) > 0:
        quote = data[0]['q'] + " - " + data[0]['a']
        return quote
    else:
        return "Couldn't fetch a quote at the moment."

def fetch_and_display_quote():
    quote_text.set(get_random_quote())

# Create the main application window
app = tk.Tk()
app.title("Random Quote App")

# Create a label to display the quote text
quote_text = tk.StringVar()
quote_label = tk.Label(app, textvariable=quote_text, wraplength=300)
quote_label.pack(pady=10)

# Create a button to fetch and display a random quote
fetch_button = tk.Button(app, text="Fetch Quote", command=fetch_and_display_quote)
fetch_button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
