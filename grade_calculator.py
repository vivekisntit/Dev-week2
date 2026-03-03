name=input("Enter your name: ")
while True:
    try:
        marks=float(input("Enter your marks (0-100): "))
        if 0 <= marks <= 100:
            break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")
        
print(f"📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print("Grade:", end=" ")
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")
print("Message: Very Good! Keep it up! 👍")
