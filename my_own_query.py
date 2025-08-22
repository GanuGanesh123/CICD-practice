
import pandas as pd
import argparse

# sample query = lavada naku col1 a pakkana unna value ivvu

class MyOwnQueryLanguage:

    def __init__(self):
        self.df = pd.read_csv("DB/CSV/requests.csv") #.db
        print(self.df.columns)

    def parse_query(self, query):
        return query.split()[3]
    
    def ivvu(self, query):
        self.parse_query(query)
        if "ivvu" in query:
            
            print(f'orey b value idhi ra - {self.df[self.df["col1"]=="a"]["col2"]}')

if __name__ == "__main__":
    obj = MyOwnQueryLanguage()
    obj.ivvu("avada naku col1 a pakkana unna value ivvu")






