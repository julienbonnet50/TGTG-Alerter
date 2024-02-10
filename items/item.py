import pandas as pd 
from IPython.display import display
from pandas import json_normalize
import tkinter as tk
import pandas as pd

class item:

    def cleanData(self, df):
        nested_columns = ['item', 'store']  # Add your column names

        # Flatten each nested column
        for column in nested_columns:
            nested_column_data = df[column]
            flattened_data = json_normalize(nested_column_data)
            df = pd.concat([df, flattened_data], axis=1)

        # Drop the original nested columns if needed
        dfAll = df.drop(nested_columns, axis=1)

        dfFinal = dfAll[['display_name','name', 'item_category', 'item_price.minor_units', 'item_value.minor_units', 'items_available']]

        colNamePrice = "item_price.minor_units"
        colNameValue = "item_value.minor_units"

        dfFinal.loc[:, colNamePrice] = dfFinal[colNamePrice] / 100
        dfFinal.loc[:, colNamePrice] = dfFinal[colNamePrice].apply(lambda x: '{:.2f}'.format(x))

        dfFinal.loc[:, colNameValue] = dfFinal[colNameValue] / 100
        dfFinal.loc[:, colNameValue] = dfFinal[colNameValue].apply(lambda x: '{:.2f}'.format(x))

        dfFinal = dfFinal.rename(columns={"display_name": "magasin", "name": "panier", "item_category" : "categorie", "item_price.minor_units" : "prix", "item_value.minor_units" : "prixInitial", "items_available" : "nbrArticles"})

        dfFinal = dfFinal.loc[dfFinal['nbrArticles'] > 0]

        dfFinal = dfFinal.sort_values(by=['nbrArticles'], ascending=False)

        dfFinal.to_csv('results/finalDf.csv')

        # Display the modified DataFrame
        return dfFinal
    

