#string  immutable , ordered, indexed, allow duplicates
#list  [] mutable ordered, indexed, allow duplicates
#tuple  () immutable ordered, indexed, allow duplicates
#set  {} mutable, unordered, no duplicates 
#dictionary  {} mutable, unordered, no duplicates, key-value pairs
#frozenset  frozenset() immutable, unordered, no duplicates

tuple1 = (1, 2, 3)
tuple2= tuple([4, 5, 6])
tuple3= (1,)

# example 

c=(1, 2, 3, 4, 5)
print(c[1:])
# c[2]=40

c=[1, 2, 3, 4, 5]
print(c[1:5])
c[2]=40
print(c)

#range(start, stop, step)
numbers = list(range(1, 11))
print(numbers)


#star pattern

for i in range(5):
    for x in range(i+1):
        print("*", end="")
    print()


# set
my_set = {1, 2, 3, 4, 5,5}  
set2 = set([4, 5, 6, 7, 8]) 

print(my_set)

#union

a={1, 2, 3}
b={3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5}
print(a | b) # {1, 2, 3, 4, 5}

#frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)

#none
x = None
print(x)

print (x is None) #True
print(x == None) #True

def my_function():
    pass
print(my_function()) #None
