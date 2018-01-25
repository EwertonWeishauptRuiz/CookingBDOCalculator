#import tkinter as tk
from tkinter import *
from tkinter import ttk

#window = tk.Tk()
window = Tk()
window.title("Beer Calculator")
window.geometry("500x400")
window.resizable(width=False, height=False)

logoFrame = Frame(window)
logoFrame.grid(column=0,row=0, sticky=(N, W, E, S))
logoFrame.columnconfigure(5, weight=1)
logoFrame.rowconfigure(5, weight=1)

introFrame = Frame(window, borderwidth=5)
introFrame.grid(column=0,row=1, sticky=(N, W, E, S), pady=10)
introFrame.columnconfigure(2, weight=1)
introFrame.rowconfigure(2, weight=1)
introFrame.config(bg="grey")

mainframe = Frame(window)
mainframe.grid(column=0, row=2, sticky=(N, W, E, S), padx= 5, pady=5)
mainframe.columnconfigure(5, weight=1)
mainframe.rowconfigure(5, weight=1)


def cookingamount(*args):    
    try:
        amount = float(vegetable.get())
        totalBeers = amount / 5
        waters = totalBeers * 6
        leaveling = totalBeers * 2
        sugar = totalBeers
        print(totalBeers)
        #Set Text on GUI
        #waterLabel.set(waters)
        #leavelingLabel.set(leaveling)
        #sugarLabel.set(sugar)
        #beersLabel(totalBeers)
    except ValueError:
        errorCode.set('Not a valid Number')
        pass

def reset():
    errorCode.set('')
    vegetable.set('')
    waterLabel.set('')
    leavelingLabel.set('')
    sugarLabel.set('')
    beersLabel('')

#Set Ingredients
vegetable = StringVar()
waterLabel = StringVar()
leavelingLabel = StringVar()
sugarLabel = StringVar()
beersLabel = StringVar()
errorCode = StringVar()
#Intro and Logo
logo = PhotoImage(file='bdo.png')
ttk.Label(logoFrame, image=logo).grid(column=3)
ttk.Label(introFrame, text='The Black Desert Beer Calculator', font="22", foreground="white", background="grey").grid(column=2)
#Vetetable Entry
vegetable_entry = ttk.Entry(mainframe, width=15, textvariable=vegetable)
vegetable_entry.grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text='Amount of Vegetables:').grid(column=0, row=1, sticky=W)
#Basic Text Setup
ttk.Label(mainframe, text='Water:').grid(sticky=E)
ttk.Label(mainframe, text='Leaveling:').grid(sticky=E)
ttk.Label(mainframe, text='Sugar:').grid(sticky=E)
ttk.Label(mainframe, text='Total Beers:').grid(sticky=E)
#Error Handleing
ttk.Label(mainframe, textvariable=errorCode, foreground="red").grid(column=1, sticky=E)

#calculate Button
calculateButton = ttk.Button(mainframe, text="Calculate", command=cookingamount)
calculateButton.grid(column=1,row=8, sticky=W)
#Reset Button
resetButton = ttk.Button(mainframe, text="Reset", command=reset)
resetButton.grid(column=2, row=8, sticky=E)

for child in mainframe.winfo_children(): 
     child.grid_configure(padx=5, pady=5)

window.mainloop()

