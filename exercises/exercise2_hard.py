# Python program for binary search

mylist = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] # makes a list
x = 8 # this is what goldilocks is looking for

# define a function
def binary_search (x, mylist, left, right):
    """This function takes some numbers and gives you some other numbers"""
    
    if left > right: # makes sure there are elements in the list
        return -1

    mid = int(round((left + right) / 2)) #calculates the midpoint

    if mylist[mid] == x: # checks if midpoint is just right!
        return mid

    elif mylist[mid] > x: # checks if midpoint is too high
        return binary_search (x, mylist, left, mid-1)

    elif mylist[mid] < x: #c checks if midpoint is too low
        return binary_search(x, mylist, mid+1, right)

print binary_search(x, mylist, 0, len(mylist)-1) # print result