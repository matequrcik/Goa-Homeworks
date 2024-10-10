"""  შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია შემდეგ გამოიტანეთ ამ ყველა რიცხვის ჯამი"""

mylist=[1,2,5,6,3,6,5,64,7453,66,567,8,6,13,34,12]


def listsum(list):
    listsum=0
    for i in range(len(mylist)):
        listsum=listsum+mylist[i]
    print(listsum)
listsum(mylist)




