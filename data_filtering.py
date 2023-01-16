import pandas as pd

df = pd.read_csv("final_data.csv")
df.head()

bools =[]
for d in df.Distance:
    if d<=100:
        bools.append(True)
    else:
        bools.append(False)

isDist = pd.Series(bools)
isDist.head()

starDist=df[isDist]

starDist.reset_index(inplace=True,drop=True)
starDist.head()
starDist.shape

gravity_bool = []
for g in starDist.Gravity:
    if g<=350 and g>=150:
        gravity_bool.append(True)
    else :
        gravity_bool.append(False)

is_gravity = pd.Series(gravity_bool)

finalStars = starDist[is_gravity]

finalStars.head()
finalStars.shape
finalStars.reset_index(inplace=True,drop=True)
finalStars.head()
finalStars.to_csv("filteredStars.csv")
