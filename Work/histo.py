import pandas
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


df = pandas.read_csv(
    "./Data/EP_Data_Extended.csv", quotechar='"', skipinitialspace=True, low_memory=False
)

print(df)
handles = df.loc[:, "handle"]
trackers = df.loc[:, "trackers"]

# Get all handles in a list
handles = handles.values.tolist()

# Get all trackers in a list
trackers_permissions = trackers.values.tolist()


dict_trackers = {}
dict_permissions = {}

# Count nb of each tracker and each permission
for el in trackers_permissions:
    if type(el) == str:
        el = el.split(",")
        for nb in el:
            if nb and nb.isdigit() and nb in dict_trackers:
                dict_trackers[nb] += 1
            elif nb and nb.isdigit():
                dict_trackers[nb] = 1
            elif "permission" in nb and nb in dict_permissions:
                dict_permissions[nb] += 1
            else:
                dict_permissions[nb] = 1


# most_permissions = sorted(dict_permissions.items(), reverse=True, key=lambda t: t[1])
# most_trackers = sorted(dict_trackers.items(), reverse=True, key=lambda t: t[1])
# print(most_trackers[0][1])


# plt.bar(list(dict_trackers.keys()), dict_trackers.values())
# plt.show()