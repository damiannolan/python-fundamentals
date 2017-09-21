# Problem 8 - Merge and Sort Lists
# 1. Create a function that accepts two lists as the arguements
# 2. Use .extend() to merge the lists
# 3. Use .sort() to sort the lists
# 4. ...
# 5. Profit

def mergeAndSort(lst, lst2):
    lst.extend(lst2)
    lst.sort()

    return lst

print(mergeAndSort([1,4,6], [2,3,5]))
