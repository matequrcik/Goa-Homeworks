def my_list(arr):
    new_list = []
    for i in arr:
        if i %2 == 0:
            new_list.append(i)
    sum = 0
    for i in new_list:
        sum = sum + i
    print(sum)
my_list([1,2,3,4])