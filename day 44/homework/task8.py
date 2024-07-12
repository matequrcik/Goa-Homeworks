"""4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list."""

list=[1,3,5,4,6,5,9]
list2=[]
i=0
len= len(list)
while i != len:
    list2.append(list[i]*2)
    i=i+1
print(list2)