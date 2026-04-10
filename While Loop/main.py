# laps = 1

# while laps <=5:
#     print(f"Lap {laps} completed")
#     laps +=1
# print("Race completed")


# Count = 1

# while Count <=10:
#     print(f"Count: {Count}")
#     Count +=1
# print("Counting completed")

number = 0

while number <= 10:
    if number == 5:
        break
    number += 1
    if number % 2 == 0:
        continue
    print(number)
# else:
#     print("completed")

# secret = 7
# while True:
#     guess = int(input("Guess the number: "))
#     if guess == secret:
#         print("Success")
#         break
#     else:
#         print("Try again")