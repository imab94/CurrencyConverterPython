import ttkbootstrap as ttk
import ttkbootstrap.dialogs
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from currency_converter import CurrencyConverter


root = ttk.Window(themename="vapor")
root.geometry("720x450+400+200")
root.title("Password Generator APP")
root.resizable(0,0)

global MenuItem1
global MenuItem2

MenuItem1 = ""
MenuItem2 = ""

countryCode = {'INDIA': 'INR', 'United State America': 'USD',"New Zealand Dollar":"NZD","Turkey Lira":"TRY","Malaysia Ringgit":"MYR",
               'Brazilian Real': 'BRL', 'Canadian Dollar': 'CAD', 'Chinese Yuan': 'CNY',"Philippines Peso":"PHP","Romania Leu":"RON",
               'Czech Koruna': 'CZK','Euro': 'EUR',"Sweden Krona":"SEK","Switzerland Franc":"CHF","Poland Zloty":"PLN",
               'Hong Kong Dollar': 'HKD', 'British Pound': 'GBP',"Thailand Baht":"THB"," Iceland Krona":"ISK","Australia Dollar":"AUD",
               "Mexico Peso":"MXN","Indonesia Rupiah":"IDR","South Korea Won":"KRW","Israel Shekel":"ILS"
               }

def selectedOption1(value1):
    global MenuItem1
    MenuItem1 = value1
    menuBar1.configure(text=value1)


def selectedOption2(value2):
    global MenuItem2
    MenuItem2 = value2
    menuBar2.configure(text=value2)


def ConvertCurrency():
    c = CurrencyConverter()
    amount = amountField.get()
    from_currency = countryCode.get(MenuItem1)
    to_currency = countryCode.get(MenuItem2)

    if not amount or not from_currency or not to_currency:
        ttkbootstrap.dialogs.Messagebox.show_error("Please select currencies and enter amount", "Error")
    else:
        if amount.isdigit():
            convertedCurrency = c.convert(amount, from_currency, to_currency)
            CurrencyLabel.config(text="Converted Currency: " + str(round(convertedCurrency,3))+" "+to_currency)
        else:
            ttkbootstrap.dialogs.Messagebox.show_error("amount must be a number", "Error")


def confirm_quit():
    response  = ttkbootstrap.dialogs.Messagebox.yesno("Are you sure you want to exit?", "Exit Window", alert=True)
    if response == "Yes":
        root.destroy()


topLabel = ttk.Label(root, text="Currency Conversion", font=('helecia', 18))
topLabel.grid(row=0, column=0, columnspan=4, padx=180, pady=10)

fromLabel = ttk.Label(root, text="From:", font=('helecia', 13),foreground="white")
fromLabel.grid(row=1, column=0, columnspan=1, padx=5, pady=30)

menuBar1 = ttk.Menubutton(root,text="select option",bootstyle="info-outline")
menuBar1.grid(row=1,column=1,padx=5,pady=30)

insideMenu1 = ttk.Menu(menuBar1)

# Adding items into menu1
item_var = ttk.StringVar()
for x in countryCode:
    insideMenu1.add_radiobutton(label=x,variable=item_var,command=lambda x=x:selectedOption1(x))

menuBar1['menu'] = insideMenu1


toLabel = ttk.Label(root, text="To:", font=('helecia', 13),foreground="white")
toLabel.grid(row=1, column=2, columnspan=1, padx=5, pady=30)

menuBar2 = ttk.Menubutton(root,text="select option",bootstyle="info-outline")
menuBar2.grid(row=1,column=3,padx=5,pady=30)

insideMenu2 = ttk.Menu(menuBar2)

# Adding items into menu1
item_var2 = ttk.StringVar()
for x in countryCode:
    insideMenu2.add_radiobutton(label=x,variable=item_var2,command=lambda x=x:selectedOption2(x))

menuBar2['menu'] = insideMenu2

# Amount Label and Entry Field

amountLabel = ttk.Label(root,text="Amount ",font=("helvica", 13),bootstyle="info")
amountLabel.grid(row=2, column=0, padx=10, pady=30,columnspan=1)

amountField = ttk.Entry(root,font=("helvica", 13),bootstyle="info")
amountField.grid(row=2, column=1, padx=10, pady=30,columnspan=2)

# Generated password label
CurrencyLabel = ttk.Label(root, text="", anchor=ttk.CENTER,font=("helvica", 13),bootstyle="info")
CurrencyLabel.grid(row=3, column=0, padx=10, pady=30,columnspan=3)

# Buttons to generate or cancel password
convert = ttk.Button(root, text="Convert",bootstyle=(SUCCESS, OUTLINE),command=ConvertCurrency)
cancel_button = ttk.Button(root, text="Cancel", command=confirm_quit,bootstyle=(DANGER, OUTLINE))

convert.grid(row=6, column=0, padx=5, pady=30,columnspan=2)
cancel_button.grid(row=6, column=2, padx=10, pady=30,columnspan=2)

root.mainloop()
