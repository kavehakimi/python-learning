import pandas as pd

data = {
    "name": ["Kaveh", "Kami", "Hoda"],
    "age": [50, 52, 43],
    "City": ["London", "Tehran", "Bristol"]
}

df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.info())
print(df.describe())
print("----------")
print(df[["name" , "age"]])
print("Mean age: ", df["age"].mean())
print("Max age: ", df["age"].max())
print("Min age: ", df["age"].min())
print(df[df["age"] >= 50])
print(df[df["age"] < 50])

