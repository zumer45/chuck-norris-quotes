from tkinter import *
from tkinter import ttk
import requests
from constants import *
def main():
    norris_api_data = getQuotes(URL)
    create_gui(norris_api_data)
    


def getQuotes(url):
    try: 
        r = requests.get(url)
        data = r.json()
        return data["value"] 
    except Exception as e:
        print(e)
    

def create_gui(quote):

    root = Tk()
    root.title("Chuck Norris Quotes")
    root.configure(bg="black")
    root.geometry("900x700")

    frame = Frame(root)
    frame.pack(expand=True)

    label = Label(frame, text=quote, wraplength=300, justify="center", fg="red")
    label.pack()
    button = ttk.Button(root, text="Get Another Quote" ,command=lambda: refresh(label))
    button.pack()
    
    
    root.mainloop()

def refresh(label):
    new_quote = getQuotes(URL)
    label.config(text= new_quote)





main()