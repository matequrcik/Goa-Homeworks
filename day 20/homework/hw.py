num1=(int(input("your 1 number: ")))
num2=(int(input("your 2 number: ")))
print(num2,  "<",  num1,  "=")
print(num2 < num1)
print(num2,  ">",  num1,  "=")
print(num2 > num1)
bool1 = input("Now, write your first boolean (true/false): ").lower() == 'true'
bool2 = input("Now, write your second boolean (true/false): ").lower() == 'true'

print("If there is 'and', the result is:", bool1 and bool2)
print("If there is 'or', the result is:", bool1 or bool2)
print("temperature is")
temp=(32)
act_on = temp > 30
print(act_on)