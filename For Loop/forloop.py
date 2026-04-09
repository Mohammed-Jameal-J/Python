fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


number =[1,2,3,4,5,6,7,8,9]

for num in number:
    if num == 5:
        continue
    if num == 7:
        break
    print(num)


fruits = ["apple", "banana", "cherry"]
for i,f in enumerate(fruits):
    print(i,f)