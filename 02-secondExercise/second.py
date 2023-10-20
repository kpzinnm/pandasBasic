import pandas as pd

def main():
    # load DataFrame
    wine_reviews = pd.read_csv('/home/gabriel/Documentos/Programação/Pandas Python/Exercicios Kaggle/data bases/dataBaseWine/winemag-data-300l.csv', index_col=0)

    # search by position
    index(wine_reviews)

    # search by label
    label(wine_reviews)

    # selection
    selection(wine_reviews)

def index(wine_reviews):
    # search by position
    print(wine_reviews.iloc[1])
    space()
    print(wine_reviews.iloc[:,3])
    space()
    print(wine_reviews.iloc[-2:])
    space()
    print(wine_reviews.iloc[[1,6,8,11],0])

def label(wine_reviews):
    # search by label
    print(wine_reviews.loc[:3,'country'])
    space()
    print(wine_reviews.loc[[1,2,3],['country','price']])
    space()
    print(wine_reviews.set_index("title"))

def selection(wine_reviews):
    # wines from France
    # print(wine_reviews.loc[wine_reviews.country == "France", 'price'])
    space()
    # The bests wines France
    print(wine_reviews.loc[((wine_reviews.country == "Australia")|(wine_reviews.country == "New Zealand"))&(wine_reviews.points >= 95)])


def space():
    print("\n- - - - - - - - - - - -\n")

main()