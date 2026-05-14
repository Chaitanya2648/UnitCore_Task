import pandas as pd

# creating data for the DataFrame
data = {
    "name"     : ["Chaitanya", "Ketan", "Shub"],
    "marks"    : [78, 67, 77],
    "fav_food" : ["biryani", "Vada Pav", "Chinese Bhel"]
}

# creating the DataFrame
df = pd.DataFrame(data)
print("The DataFrame is:")
print(df)

# filtering students with marks greater than 70
high_marks = df[df["marks"] > 70]
print("the students having marks greater than 70 is:")
print(high_marks)

# getting the shape (rows, columns) of the full DataFrame
rows = df.shape
print("the rows of marks and name are:")
print(rows)

# getting the shape (rows, columns) again for columns count
cols = df.shape
print("the column of marks and name are:")
print(cols)