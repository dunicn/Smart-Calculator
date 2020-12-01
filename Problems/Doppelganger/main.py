# the object_list has already been defined
# write your code here
from collections.abc import Hashable

newlist = []
counter = 0
counts = dict()
for x in object_list:
    if isinstance(x, Hashable):
        h_number = x.__hash__()
        if h_number in counts:
            counts[h_number] += 1
        else:
            counts[h_number] = 1
for x in counts:
    if counts[x] > 1:
        counter += counts[x]
print(counter)
