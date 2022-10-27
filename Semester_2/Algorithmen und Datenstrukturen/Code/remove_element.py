"""
statisches Array X mit N Elementen
PseudoCode, um Element an Index i zu löschen
-> Laufzeit und Speicherbedarf analysieren
"""


# initial values
old_array = list(range(10))
del_index = 7

# copy all values before the deleted element from old array to new array
new_array = [None] * (len(old_array) - 1)
new_array[:del_index] = old_array[:del_index].copy()

# copy all values after the deleted element with shifted index
for idx in range(del_index, len(old_array) - 1):
    new_array[idx] = old_array[idx + 1]

print(new_array)

# Best-Case: Element is last one, we would only need to copy (n insertions) --> O(n)
# Worst-Case: Element is first one: we first copy all elements and then update the element (2n insertions) --> O(n)
# Average-Case: --> O(n)
