# Project: Basic Search App
# Application developed by: Jake - September 2024
# Learning Python programming with the assistance of AI and online courses

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import webbrowser

# Constants
PEXELS_API_KEY = 'QSIs6uQZNOCdh6VlD97eLDwJim1PcLM1TM2nxtGInHV1ZV0Yitgjcp03'
PEXELS_URL = "https://api.pexels.com/v1/search"
WIKI_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"
WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"

# Fetch and display an image from Pexels
def fetch_image(query):
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page': 10}

    try:
        response = requests.get(PEXELS_URL, headers=headers, params=params)
        response.raise_for_status()
        photos = response.json().get('photos', [])

        if photos:
            image_url = random.choice(photos)['src']['medium']
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image = Image.open(BytesIO(image_response.content))
            return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error fetching image: {e}")
    return None

# Generate Wikipedia link
def facts_link(query):
    return f"{WIKI_BASE_URL}{query.replace(' ', '_')}"

# Fetch summary from Wikipedia
def fetch_summary(query):
    try:
        response = requests.get(WIKI_SUMMARY_URL + query)
        response.raise_for_status()
        data = response.json()
        return data.get('extract', "Summary not available.")
    except Exception as e:
        print(f"Error fetching summary: {e}")
        return "Error fetching summary."

# Handle button click event
def on_button_click():
    query = entry.get().strip().replace(' ', '_')
    summary = fetch_summary(query)

    # Update the summary text and fact link
    summary_label.config(text=summary)
    fact_link_label.config(text=f"Click here for more information about {entry.get()}", cursor="hand2")
    fact_link_label.bind("<Button-1>", lambda e: webbrowser.open(facts_link(query)))

    # Fetch and display the image
    photo = fetch_image(entry.get())
    if photo:
        canvas.image = photo  # Keep a reference to avoid garbage collection
        canvas.config(width=photo.width(), height=photo.height())
        canvas.create_image(photo.width() // 2, photo.height() // 2, image=photo, anchor=tk.CENTER)
        canvas.grid(row=4, column=0, columnspan=2, pady=(0, 20), sticky="nsew")  # Ensure canvas is shown
    else:
        canvas.config(width=200, height=200)  # Default size when no image is found
        canvas.create_text(100, 100, text="Image not found", fill="black", anchor=tk.CENTER)
        canvas.grid(row=4, column=0, columnspan=2, pady=(0, 20), sticky="nsew")  # Ensure canvas is shown

    # Clear the entry widget
    entry.delete(0, tk.END)

def on_enter(event):
    on_button_click()

# Main application window setup
root = tk.Tk()
root.title("Basic Search App")
root.configure(bg="#f0f2f5")

# Load and display the top image
top_image_url = "https://www.metroparks.org/wp-content/uploads/2021/05/explore-logo.png"
top_image_response = requests.get(top_image_url)
top_image = Image.open(BytesIO(top_image_response.content)).resize((350, 200), Image.Resampling.LANCZOS)
top_photo = ImageTk.PhotoImage(top_image)
tk.Label(root, image=top_photo).pack(pady=(0, 10))

# Main frame for content
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill='both', expand=True)

# Styling
style = ttk.Style()
style.configure('TButton', padding=10, relief="flat", background="#007BFF", foreground="white", font=("Calibri", 12, "bold"))
style.configure('TEntry', fieldbackground='#ffffff', foreground='black', borderwidth=2)

# Add a centered main title label
ttk.Label(main_frame, text="Search for images and facts", font=("Calibri", 20), anchor="center").grid(
    row=0, column=0, columnspan=2, pady=(0, 10), sticky="nsew"
)

# Entry field
entry = ttk.Entry(main_frame, font=("Calibri", 16), justify='center', style='TEntry')
entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")

# Custom styled button
button_canvas = tk.Canvas(main_frame, width=200, height=50, bg="#007BFF", highlightthickness=0)
button_canvas.create_rectangle(0, 0, 200, 50, fill="#007BFF", outline="#0056b3", width=2)
button_canvas.create_text(100, 25, text="Search", fill="white", font=("Calibri", 14, "bold"))
button_canvas.grid(row=2, column=0, columnspan=2, pady=10)
button_canvas.bind("<Button-1>", lambda e: on_button_click())

# Canvas for images
canvas = tk.Canvas(main_frame, bg="#ffffff", highlightthickness=0)
canvas.grid(row=4, column=0, columnspan=2, pady=(0, 20), sticky="nsew")
canvas.grid_forget()

# Summary label
summary_label = tk.Label(main_frame, font=("Calibri", 11), wraplength=550, justify='left')
summary_label.grid(row=3, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

# Update the fact link label to be centered
fact_link_label = ttk.Label(
    main_frame,
    text="",
    anchor="center",
    font=("Calibri", 12, "underline"),
    foreground="#007BFF",
    justify="center"
)
fact_link_label.grid(row=5, column=0, columnspan=2, pady=(0, 5), sticky="nsew")

# Footer label
ttk.Label(root, text="Application developed by: Jake - 2024", font=("Calibri", 8), foreground="#333333").pack(side="bottom", pady=(5, 10))

# Grid configuration
main_frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
main_frame.grid_columnconfigure([0, 1], weight=1)

# Bind Enter key to button click
root.bind('<Return>', on_enter)

# Start the application
root.mainloop()
