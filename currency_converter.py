import tkinter as tk
from tkinter import ttk, messagebox
import requests

# 🔑 Replace with your API key from exchangerate-api.com
API_KEY = "abf09d198c6af8e93f1ad13a"

API_URL = "https://v6.exchangerate-api.com/v6/abf09d198c6af8e93f1ad13a/latest/USD"

# 🌍 Supported currency codes
CURRENCIES = ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "SGD", "JPY", "CNY", "ZAR"]

# 📡 Function to get exchange rate
def get_exchange_rate(from_currency, to_currency):
    try:
        url = API_URL.format(API_KEY, from_currency)
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"].get(to_currency)
        return None
    except:
        return None

# 🔁 Convert button function
def convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency_cb.get()
        to_curr = to_currency_cb.get()

        if not from_curr or not to_curr:
            messagebox.showwarning("Missing Info", "Please select both currencies.")
            return

        rate = get_exchange_rate(from_curr, to_curr)
        if rate:
            converted = amount * rate
            result_label.config(
                text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
            )
        else:
            messagebox.showerror("Error", "Couldn't fetch exchange rate. Check API key or internet.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")

# 🎨 GUI setup
root = tk.Tk()
root.title("🌍 Currency Converter")
root.geometry("400x300")
root.configure(bg="#eef2f7")

# 🏷 Title
tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"), bg="#eef2f7", fg="#333").pack(pady=15)

# 💰 Amount Entry
tk.Label(root, text="Amount", font=("Arial", 12), bg="#eef2f7").pack()
amount_entry = tk.Entry(root, font=("Arial", 12), justify="center")
amount_entry.pack(pady=5)

# 🔄 Currency Selection Frame
frame = tk.Frame(root, bg="#eef2f7")
frame.pack(pady=10)

tk.Label(frame, text="From", font=("Arial", 11), bg="#eef2f7").grid(row=0, column=0, padx=10)
from_currency_cb = ttk.Combobox(frame, values=CURRENCIES, state="readonly")
from_currency_cb.grid(row=0, column=1)

tk.Label(frame, text="To", font=("Arial", 11), bg="#eef2f7").grid(row=1, column=0, padx=10, pady=5)
to_currency_cb = ttk.Combobox(frame, values=CURRENCIES, state="readonly")
to_currency_cb.grid(row=1, column=1)

# 🔘 Convert Button
tk.Button(root, text="Convert", command=convert, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=2).pack(pady=10)

# 📊 Result Display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#eef2f7", fg="#333")
result_label.pack(pady=10)

root.mainloop()
