def mergeAndSort(lst, lst2):
    lst.extend(lst2)
    lst.sort()

    return lst

print(mergeAndSort([1,4,6], [2,3,5]))
