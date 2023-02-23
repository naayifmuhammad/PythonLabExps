# 3. Write a python function that takes two lists and returns True if they have at least one
# common member

def compareLists(list1,list2):
    for element in list1:
        if element in list2:
            return True
    return False

list1 = input("Enter elements for list 1[Type elements seperated by a whitespace]: ").split()
list2 = input("Enter elements for list 2[Type elements seperated by a whitespace]: ").split()
if compareLists(list1,list2):
    print("There is a common element")
else:
    print("There is no common element")
