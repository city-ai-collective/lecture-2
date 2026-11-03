print("Hello, World!")

user_val = input("Enter your name: ")
print(f"Your name is: {user_val}")

score = int(input("What did you get in FR2101?"))

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
else:
    print("Pass")
    
for i in range(1,101):
    print(f"Item: {i}")