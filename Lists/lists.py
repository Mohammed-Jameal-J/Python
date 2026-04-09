fruits =["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
print(fruits[0])
print(fruits[-1])

#list slicing
print(fruits[1:4])
print(fruits[::2])


#list concat
more_fruits = ["fig", "grape"]
all_fruits = fruits + more_fruits
print(all_fruits)

#pop , insert , remove , append , sort , reverse , extend , clear , index , count
fruits.append("honeydew")
print(fruits)
print(fruits.index("apple"))
fruits.insert(2, "coconut")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.extend(["kiwi", "lemon"])
print(fruits)
fruits.clear()
print(fruits)
fruits.count("apple")
print(fruits.count("apple"))




a=[1, 2, 3]
b=a.copy()
# b = a[:]
# b = list(a)

b[0] =3

print(a)
print(b)

print(len(fruits))