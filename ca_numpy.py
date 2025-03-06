# # question 1
# import numpy as np
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
# array = np.array([a, b])
# print("Second row of the second matrix:", array[1, 1])
# print("Element at (3,3) of the 1st matrix:", array[0, 2, 2])



# # question 2
# import pandas as pd
# my_data = {
#     'ID': [1, 2, 3, 4, 5, 6, 7, 8],
#     'Color': ['Black', 'Yellow', 'Yellow', 'Blue', 'Blue', None, 'Yellow', None],
#     'Value': [80, 100, 120, 90, 85, 60, 100, 40],
#     'Flag': ['Yes', 'No', 'Yes', 'No', 'No', 'No', None, None],
#     'Category': [1, 2, 2, 2, None, 1, 2, 1]
# }
# df = pd.DataFrame(my_data)
# print("Original DataFrame:")
# print(df)
# df['Color'].fillna(df['Color'].mode()[0], inplace=True)

# df['Flag'].fillna(df['Flag'].mode()[0], inplace=True)

# df['Category'].fillna(df['Category'].median(), inplace=True)

# print("\nProcessed DataFrame:")
# print(df)

# question 3
import pandas as pd

my_data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Color': ['Black', 'Yellow', 'Yellow', 'Blue', 'Blue', None, 'Yellow', None],
    'Value': [80, 100, 120, 90, 85, 60, 100, 40],
    'Flag': ['Yes', 'No', 'Yes', 'No', 'No', 'No', None, None],
    'Category': [1, 2, 2, 2, None, 1, 2, 1]
}

df = pd.DataFrame(my_data)

df['Color'].fillna(df['Color'].mode()[0], inplace=True)
df['Flag'].fillna(df['Flag'].mode()[0], inplace=True)
df['Category'].fillna(df['Category'].median(), inplace=True)

highest_weights = df.loc[df.groupby('Color')['Value'].idxmax()].sort_values(by='Value')[['Color', 'Value']]
print(highest_weights)
