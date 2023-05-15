import tkinter as tk


def clear():
    window.title("Введите домашний адрес!")
    name_entry.delete("0", tk.END)
    surname_entry.delete("0", tk.END)
    address_1_entry.delete("0", tk.END)
    address_2_entry.delete("0", tk.END)
    city_entry.delete("0", tk.END)
    county_entry.delete("0", tk.END)
    country_entry.delete("0", tk.END)
    postcode_entry.delete("0", tk.END)
    country_entry.delete("0", tk.END)
    window.focus()


def send():
    window.title(f"{name_entry.get()}, , ваши данные успешно отправлены")


window = tk.Tk()
window.title("Введите домашний адрес!")
window.geometry("400x300+300+300")

frame_main = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_main.pack(fill=tk.X)

frame_btn = tk.Frame()
frame_btn.pack(fill=tk.X)

name = tk.Label(frame_main, text="Имя:", anchor="e")
name.grid(column=0, row=0, columnspan=2, sticky="new", pady=5, padx=5)

name_entry = tk.Entry(frame_main, width=45)
name_entry.grid(column=2, row=0, columnspan=2, sticky="new", pady=5, padx=5)

surname = tk.Label(frame_main, text="Фамилия:", anchor="e")
surname .grid(column=0, row=1, columnspan=2, sticky="new", pady=5, padx=5)

surname_entry = tk.Entry(frame_main, width=45)
surname_entry.grid(column=2, row=1, columnspan=2, sticky="new", pady=5, padx=5)

address_1 = tk.Label(frame_main, text="Адрес 1:", anchor="e")
address_1.grid(column=0, row=2, columnspan=2, sticky="new", pady=5, padx=5)

address_1_entry = tk.Entry(frame_main, width=45)
address_1_entry.grid(column=2, row=2, columnspan=2, sticky="new", pady=5, padx=5)

address_2 = tk.Label(frame_main, text="Адрес 2:", anchor="e")
address_2.grid(column=0, row=3, columnspan=2, sticky="new", pady=5, padx=5)

address_2_entry = tk.Entry(frame_main, width=45)
address_2_entry.grid(column=2, row=3, columnspan=2, sticky="new", pady=5, padx=5)

city = tk.Label(frame_main, text="Город:", anchor="e")
city.grid(column=0, row=4, columnspan=2, sticky="new", pady=5, padx=5)

city_entry = tk.Entry(frame_main, width=45)
city_entry.grid(column=2, row=4, columnspan=2, sticky="new", pady=5, padx=5)

county = tk.Label(frame_main, text="Регион:", anchor="e")
county.grid(column=0, row=5, columnspan=2, sticky="new", pady=5, padx=5)

county_entry = tk.Entry(frame_main, width=45)
county_entry.grid(column=2, row=5, columnspan=2, sticky="new", pady=5, padx=5)

postcode = tk.Label(frame_main, text="Почтовый индекс:", anchor="e")
postcode.grid(column=0, row=6, columnspan=2, sticky="new", pady=5, padx=5)

postcode_entry = tk.Entry(frame_main, width=45)
postcode_entry.grid(column=2, row=6, columnspan=2, sticky="new", pady=5, padx=5)

country = tk.Label(frame_main, text="Страна:", anchor="e")
country.grid(column=0, row=7, columnspan=2, sticky="new", pady=5, padx=5)

country_entry = tk.Entry(frame_main, width=45)
country_entry.grid(column=2, row=7, columnspan=2, sticky="new", pady=5, padx=5)

send_btn = tk.Button(frame_btn, text="Отправить", command=send)
send_btn.pack(side=tk.RIGHT, padx=5)

clear_btn = tk.Button(frame_btn, text="Очистить", command=clear)
clear_btn.pack(side=tk.RIGHT, padx=5)


window.mainloop()
