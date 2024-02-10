from typing import ItemsView
from tgtg import TgtgClient
from items.item import item
import pandas as pd 
import time
import tkinter as tk
from tkinter import ttk

class DataFrameViewer(tk.Tk):
    def __init__(self, dataframe, title="DataFrame Viewer"):
        super().__init__()
        self.title(title)
        self.dataframe = dataframe
        self.cols = list(dataframe.columns)
        ttk.Style().theme_use("clam")

        self.tree = ttk.Treeview(self)
        self.tree.tag_configure("evenrow", background="#f0f0f0")  # Background color for even rows
        self.tree.tag_configure("oddrow", background="#ffffff")  # Background color for odd rows
        self.tree.pack(expand=True, fill="both")
        self.tree["columns"] = self.cols

        for col in self.cols:
            self.tree.column(col, anchor="w", width=100)
            self.tree.heading(col, text=col, anchor='w')

        self.update_treeview()
        self.after(2000, self.load_and_update)  # Schedule the load_and_update method every 2000 milliseconds (2 seconds)

    def update_treeview(self):
        # Clear the existing data in the tree
        self.tree.delete(*self.tree.get_children())

        # Insert new data into the tree
        for index, row in self.dataframe.iterrows():
            self.tree.insert("", tk.END, text=index, values=list(row))

    def load_and_update(self):
        self.dataframe = getAndPrintItems()

        # Update the Treeview with the new DataFrame
        self.update_treeview()

        # Schedule the load_and_update method every 2000 milliseconds (2 seconds)
        self.after(ItemsView.constant.FIVE_MINUTES, self.load_and_update)

# client = TgtgClient(email="julienbonnet50@gmail.com")
# credentials = client.get_credentials()
item = item()

def getAndPrintItems():
    # You can then get some items, by default it will *only* get your favorites
    items = client.get_items()

    # To get items (not only your favorites) you need to provide location informations
    items = client.get_items(
        favorites_only=False,
        latitude=48.838,
        longitude=2.48,
        radius=1,
    )
    dfTgTg = pd.DataFrame(items)

    return item.cleanData(dfTgTg)

sample = {
        "magasin": [f"Initial dataframe to be updated... ({i})" for i in range(5)],
        "panier": [f"Initial dataframe to be updated... ({i})" for i in range(5)],
        "categorie": [f"Initial dataframe to be updated... ({i})" for i in range(5)],
        "prix": [f"Initial dataframe to be updated... ({i})" for i in range(5)],
        "prixInitial": [f"Initial dataframe to be updated... ({i})" for i in range(5)],
        "nbrArticles": [f"Initial dataframe to be updated... ({i})" for i in range(5)]
    }

df = pd.DataFrame(sample)

app = DataFrameViewer(df, "TGTG - Notifier")
app.mainloop()

