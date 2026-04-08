is_raining = True

if is_raining:
    print("take umberella")
else:
    print("enjoy")

age = int(input(" enter your age:"))

if age >=18:
    print("you can vote")
else:
    print("you cannot vote")


# ternary operator 
age = int(input(" enter your age:"))

status="adult" if age >=18 else "minor"
print(status)
