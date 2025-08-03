# app.py
import tkinter as tk
from main import get_sakha_reply  # Import the function from main.py

def respond_to_user_input():
    user_input = user_input_entry.get()
    if user_input.strip() == "":
        return
    response = get_sakha_reply(user_input)
    
    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.insert(tk.END, f"Sakha: {response}\n\n")
    
    user_input_entry.delete(0, tk.END)

# UI code continues here...
