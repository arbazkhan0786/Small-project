from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data =  a.convert(amount,cur1,cur2,)
    l5 = tk.Label(window,text= data).place(x = 230, y = 290)


l1 = tk.Label(window,text="currency converter", font= "Times 20 bold").place(x = 110, y = 40) 
l2 = tk.Label(window,text="enter amount here:", font= "Times 18 bold").place(x = 60, y = 80)
e1 = tk.Entry(window)

l3 = tk.Label(window,text="enter currency  :", font= "Times 18 bold").place(x = 60, y = 130)
e2 = tk.Entry(window)
l4 = tk.Label(window,text="enter req currency :", font= "Times 18 bold").place(x = 60, y = 180)
e3 = tk.Entry(window)

b1 = tk.Button(window,text="click", command= clicked).place(x = 230, y = 240)
e1.place(x = 300, y = 90)
e2.place(x = 300, y = 140)
e3.place(x = 300, y =190)

window.mainloop()


#a = CurrencyConverter()
#print(a.convert(12,"USD","INR"))

