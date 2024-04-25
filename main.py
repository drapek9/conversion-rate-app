from tkinter import *
import requests

window = Tk()
window.title("Převod měn 2.0")
window.geometry("400x140")
window.resizable(False, False)
window.iconbitmap("img/ico.ico")

main_font = ("Arial", 12)
main_color = "#5d85a7"
button_color = "#1a252f"
active_color = "#263745"
window.config(bg=main_color)


def count():
    try:
        from_currency = drop_down_from.get()
        to_currency = drop_down_to.get()
        amount = float(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "ANr7zTlF9RiWNWo0JBRWFXnHjV4qSQo7"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        result = response.json()
        data = round(result["result"], 2)

        result_label.config(text=data)

        no_result_label.config(text="")

    except:
        no_result_label.config(text="Zadejte prosím částku")


user_input = Entry(window, font=("Arial", 12, "bold"), width=20, justify=CENTER, borderwidth=1)
user_input.grid(row=0, column=0, padx=10, pady=10)

drop_down_from = StringVar(window)
drop_down_from.set("CZK")
drop_down_from_options = OptionMenu(window, drop_down_from, "CZK", "EUR", "USD")
drop_down_from_options.config(font=main_font, bg=button_color, activebackground=active_color, fg="white",
                              highlightthickness=0)
drop_down_from_options.grid(row=0, column=1, pady=10)

drop_down_to = StringVar(window)
drop_down_to.set("EUR")
drop_down_to_option = OptionMenu(window, drop_down_to, "EUR", "USD", "CZK")
drop_down_to_option.config(font=main_font, bg=button_color, fg="white", activebackground=active_color,
                           highlightthickness=0)
drop_down_to_option.grid(row=1, column=1)

result_label = Label(window, font=("Arial", 14, "bold"), bg=main_color, text=0)
result_label.grid(row=1, column=0)

result_button = Button(window, font=main_font, bg=button_color, fg="white", activebackground=active_color,
                       text="Přepočítat", command=count)
result_button.grid(row=0, column=2, pady=10, padx=10)

no_result_label = Label(window, font=main_font, bg=main_color)
no_result_label.grid(row=3, column=0, pady=(10, 0))

author_label = Label(window, text="Šimon Drápal 24.11.2023", bg=main_color, font=("Arial", 7))
author_label.place(x=280, y=120)

window.mainloop()
