import pandas as pd

df = pd.read_csv("Libary.csv")

array = []
for index, row in df.iterrows():
    genre = row["Genre"]
    inside = False
    genre = genre.split("/")
    for gen in genre:
        if gen not in array:
            array.append(gen)

len = len(array)

string = ""
for item in array:
    string += item + ","

string = string[:-1]
print(string)
zeros = "0," * len
zeros = zeros[:-1]
print(zeros)