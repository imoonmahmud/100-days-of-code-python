import pandas as pd

data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

count = [0, 0, 0]
for color in data['Primary Fur Color']:
    if color == 'Gray':
        count[0] += 1
    elif color == 'Cinnamon':
        count[1] += 1
    elif color == 'Black':
        count[2] += 1
print(count)

df = pd.DataFrame(
    {
        'Fur Color': ['grey', 'red', 'black'],
        'Count': count
    }
)
df.to_csv('./squirrel_count.csv')