a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

maxNum = max(a,b)

while True:
    if maxNum%a == 0 and maxNum%b == 0:
        break
    maxNum = maxNum + 1

print(f"The LCM of {a} and {b} is {maxNum}")