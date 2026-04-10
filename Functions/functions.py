def math(a,b): #paramter
    return a+b
print(math(2,3)) #argument


# 1. positional arguments

def greet(animal, name="friend"): #default argument
    return f"Hello {name}, you are a {animal}!"
print(greet("dog", "Buddy")) #positional arguments

# 2. keyword arguments
print(greet(name="style", animal="cat")) #keyword arguments

# 3. default arguments
print(greet(animal="leopard"))

# 4. variable-length arguments
def sum_numbers(*args): #tuple of variable-length arguments
  total =0
  for num in args:
     total += num
     
  return total

print(sum_numbers(1,2,3,4,5))

def print_info(**kwargs):  #dictionary of keyword arguments
   for key, value in kwargs.items():
       print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

#varable scope

x= 10 #global variable
def my_function():
    y = 5 #local variable
    print(f"Inside the function, x: {x}, y: {y}")
my_function()
print(f"Outside the function, x: {x}")

#lambda function
square = lambda x: x**2
print(square(5))