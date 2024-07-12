#3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.

for num in range(100+1):
    if num %2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")