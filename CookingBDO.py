import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Beer Calculator")
window.geometry("500x800")

logo = tk.PhotoImage(file='bdo.png')
imageTitle = tk.Label( image=logo, justify=tk.CENTER)
imageTitle.grid()
title = tk.Label(text='The BDO cooking calculator', fg='green',font=("Arial Bold", 22), height=2)
title.grid(column=0, row=0)
inQuantities = tk.Label(text='Quantities: ')
inQuantities.grid(column=0, row=1)
entry_field = tk.Entry(bd = 2)
entry_field.grid(column=0, row=1)


def cookingAmount():    
    waitForInput()
    totalBeers = amount / 5
    waters = totalBeers * 6
    leaveling = totalBeers * 2
    print('You will need: \n    - Mineral Waters:', waters, '\n    - Leaveling Agents:', leaveling, '\n    - Sugars:', totalBeers)
    print('You will make', totalBeers, 'total beers!')
    input("\n Press Enter to quit...")
    quit()

def waitForInput():
    try:
        global amount    
        amount = int(input("Input the amount of Vegetables: "))    
    except ValueError:
        print('Not a Valid Number')
        waitForInput()
        
#cookingAmount()

window.mainloop()

