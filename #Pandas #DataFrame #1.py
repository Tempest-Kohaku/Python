import pandas as pd
data = {"Name" : ["Navneet","Rohan","Saurav","Manas"],
        "Age" : [18,24,86,19],
        "City" : ["Mumbai","Thane","Andheri","Dubai"]
        }
df1 = pd.DataFrame(data)
print("The First Data frame is : ")
print(df1)
df2 = pd.DataFrame({"Name" : ["Navneet","Rohan","Saurav","Manas"],
        "Age" : [18,24,86,19],
        "City" : ["Mumbai","Nashik","Andheri","Nagpur"]
        })
print("The Second Data Frame is : ")
print(df2)
