import pandas as pd
def main():
    pd.set_option('display.max_rows', 5)
    #from learntools.core import binder; binder.bind(globals())
    #from learntools.pandas.creating_reading_and_writing import *
    print("Setup complete.")

    # Ex1 create data frame fruits
    fruits = pd.DataFrame({'Apples':[30,41],'Bananas':[21,31]},index=['2017 Sales','2018 Sales'])
    print(fruits)
    space()

    # Ex2 create series ingredients
    ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour','Milk','Eggs','Spam'],name='Dinner')
    print(ingredients)
    space()

    # Ex3 read csv
    # wine_reviews = pd.read_csv('/home/gabriel/Documentos/Programação/Pandas Python/Exercicios Kaggle/data bases/dataBaseWine/winemag-data_first150k.csv', index_col=0)
    # print(wine_reviews.tail())

    # Ex4 saving DataFrame to disk
    fruits.to_csv('frutis.csv')

def space():
    print("\n- - - - - - - - - - - -\n")

main()