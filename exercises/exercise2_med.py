# Python program to calculate mean from a list

a = [66.25, 333, 333, 1, 1234.5] # create a list of numbers
count = 0 # initializing count of numbers
total = 0 # initializing running total

for i in a:
    count = count + 1 # increment count
    total = total + i # add to running total
ave = total / count # divide total by count
print(ave) # output the result.