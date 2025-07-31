import pandas as pd
# import statement
data = {
        'Name': ['Sai', 'venkat', 'John'],
        'Age': [20, 19, 22],
        'City': ['New York', 'London', 'Paris']
    }

df = pd.DataFrame(data)
print(df.shape)
