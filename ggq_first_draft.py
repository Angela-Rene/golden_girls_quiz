

print("-------------------------------------\nWhich Golden Girls character are you?\n--------------------------------------")
print("Are you a Dorothy, Rose, Blanche, or Sophia? \nTake this quiz to find out!!\n--------------------------------------")


score = 0
print("Please answer the following questions with A, B, C, or D\n-----------------------------------")

answer1 = str(input("1. First, where would you like to live?\n  A- New York City.\n  B- On a farm, with plenty of snow.\n  C- A big, fancy house in the south.\n  D- Anywhere but the retirement home!\n")).upper()
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

answer2 = str(input("2. Which job would you prefer?\n  A- cooking delicious food\n  B- a grief counselor)\n  C- teaching children\n  D- assistant in an art museum\n")).upper()
if answer2 == "A":
    score += 1
elif answer2 == "B":
    score += 3
elif answer2 == "C":
    score += 4
elif answer2 == "D":
    score += 2
else:
    print("Please choose 'A', 'B', 'C', or 'D'")
    
print(score)
print("---------------------------------")

answer3 = str(input("3. What is your favorite thing to drink?\n  A) milk\n  B) scotch\n  C) margarita\n  D) wine\n")).upper()
if answer3 == "A":
    score += 3
elif answer3 == "B":
    score += 4
elif answer3 == "C":
    score += 2
elif answer3 == "D":
    score += 1
else:
    print("Please choose 'A', 'B', 'C', or 'D'")

print(score)
print("---------------------------------")


answer4 = str(input("4. Other than cheesecake, what is your favorite food?\n  A) Lasagna \n  B) Cookies with tea\n  C) No cheesecake? Then cheeseballs!\n  D) I find it ridiculous that cheesecake is not an option.\n")).upper()
if answer4 == "A":
    score += 1
elif answer4 == "B":
    score += 2
elif answer4 == "C":
    score += 3
elif answer4 == "D":
    score += 4
else:
    print("Please choose 'A', 'B', 'C', or 'D'")

print(score)
print("---------------------------------")

answer5 = str(input("5. You're going out for errands, and maybe some lunch. What outfit do you wear?\n  A) Something down-home and practical\n  B) A tailored, pulled together look\n  C) Something soft, sexy, and flowing\n  D) Comfort over everything else\n")).upper()
if answer5 == "A":
    score += 3
elif answer5 == "B":
    score += 4
elif answer5 == "C":
    score += 2
elif answer5 == "D":
    score += 1
else:
    print("Please choose 'A', 'B', 'C', or 'D'")
    
print(score)
print("--------------------------------")

answer6 = str(input("6. What color is that outfit?\n  A) Navy blue\n  B) Emerald green\n  C) Vibrant yellow\n  D) Classic black\n")).upper()
if answer6 == "A":
    score += 4
elif answer6 == "B":
    score += 2
elif answer6 == "C":
    score += 3
elif answer6 == "D":
    score += 1
else:
    print("Please choose 'A', 'B', 'C', or 'D'")
    
print(score)
print("----------------------------------")

answer7 = str(input("7. And finally, your friend needs some advice about an important decision. You respond by:\n  A) Telling them a humurous story from your past, whether or not it is relevant.\n  B) Giving them practical advice, since you are obviously the voice of reason.\n  C) Telling an outrageous, made-up story to make sure your point gets accross.\n  D) Talking about your own problem that is clearly more important.\n")).upper()
if answer7 == "A":
    score += 3
elif answer7 == "B":
    score += 4
elif answer7 == "C":
    score += 1
elif answer7 == "D":
    score += 2
else:
    print("Please choose 'A', 'B', 'C', or 'D'")
    
print(score)
print("---------------------------------")



print("The results are in!")

if score >= 7 and score <12:
    print("You are a Sophia!\nYour quick-witted staight talk is as sharp as your recipes are delicious!  You've seen a lot, and don't put up with nonsense. Good for you!")
elif score >= 12 and score < 18:
    print("You are a Blanche!\nYou're the southern belle type. And though you can be self-absorbed, you are confident and fearless to go after what you want!")
elif score >= 18 and score < 24:
    print("You are a Rose!\nYou are sweet, kind, and a bit naive.  But you have the best stories! Keep spreading all the sunshine!")
elif score >= 24:
    print("You are a Dorothy!\nYou are quick-witted, short-tempered, and very practical. Keep being the loyal friend that makes sure stuff gets done!")


# the scoring:

# total 24-28: Dorothy= D, 4pts each

# total 18-23: Rose= R, 3pts each

# total 12-17: Blanche= B, 2pts each

# total 7-11: Sophia= S, 1pt each
