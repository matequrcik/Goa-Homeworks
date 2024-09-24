def odd_and_even(arr):
    odd_list = []
    even_list = []
    for i in arr:
        if i %2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(odd_list)
    print(even_list)