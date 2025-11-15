#reading info from planets.txt, storing the objects in array
##import pandas as pd
##df = pd.read_csv("C:\\Users\\molly\\space-hackdash\\textfiles\\planets.txt")
##df.head()
#with open closes the text file after reading it
with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

