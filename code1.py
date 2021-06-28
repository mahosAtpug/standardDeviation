import csv
import math
import pandas as pd
import plotly.express as px
with open ("class2.csv" , newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)


file_data.pop(0)
totalEntries = len(file_data)
totalEntries
totalMarks = 0
for marks in file_data:
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries
print("This is your Mean: " , mean)
df = pd.read_csv("class2.csv")
fig = px.scatter(df , x = "Student Number" , y = "Marks")
fig.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean,
        y1 = mean,
        x0 = 0,
        x1 = totalEntries
    )
])
fig.show()
marks = file_data[1]
squaredList = []
for number in marks:
    a = int(number) - mean
    a = a**2
    squaredList.append(a)

sum = 0
for value in squaredList:
    sum += value

result = sum/(totalEntries-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)

