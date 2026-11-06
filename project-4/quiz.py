score = 0

print("General Knowledge Quiz")
print()

a = input("What is the capital of France? ").strip().lower()
if a == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is Paris.")

a = input("Which planet is known as the Red Planet? ").strip().lower()
if a == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is Mars.")

a = input("How many continents are there? ").strip().lower()
if a == "7" or a == "seven":
    print("Correct!")
    score += 1
else:
    print("Wrong. The answer is 7.")

print()
print(f"Your final score is {score}/3")