

print("-------------------------------------\nWhich Golden Girls character are you?\n--------------------------------------")
print("Are you a Dorothy, Rose, Blanche, or Sophia? \nTake this quiz to find out!!\n--------------------------------------")


score = 0

answer1 = str(input("1. First, where would you like to live?\n  A- New York City.\n  B- On a farm, with plenty of snow.\n  C- A big, fancy house in the south.\n  D- Anywhere but the retirement home!")).upper
if answer1 == "A":
    score += 4
elif answer1 == "B":
    score += 3
elif answer1 == "C":
    score += 2
elif answer1 == "D":
    score += 1
else:
    print("Please choose 'A', 'B', 'C', or 'D'")

print(score)
print("----------------------------------")
answer2 = str(input("2. Which job would you prefer?\n  A- cooking delicious food (S,1)\n  B- a grief counselor (R,3)\n  C- teaching children (D,4)\n  D- assistant in an art museum (B,2)")).upper
if answer1 == "A":
    score += 1
elif answer1 == "B":
    score += 3
elif answer1 == "C":
    score += 4
elif answer1 == "D":
    score += 2
else:
    print("Please choose 'A', 'B', 'C', or 'D'")
    
