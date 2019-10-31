import pandas as pd

#read in csv
df = pd.read_csv('titanic.csv')
#create a list of Age Values
#not including N/A Values
ls_age = df['Age'].dropna()
ls_gender = df['Sex'].dropna()

# Methods

def get_sum(ls):
    total = 0
    for val in ls:
        total += val
    return total

def get_avg(ls):
    total = get_sum(ls)
    return total/len(ls)

def get_percent_female(ls):
    total = len(ls)
    females = 0
    for gender in ls:
        if gender == "female":
            females += 1
    return (females / total) * 100

def get_70_percent_age(ls):
    

# Method Calls/Main
print("average age {}".format(get_avg(ls_age)))
print("% of females {}".format(get_percent_female(ls_gender)))