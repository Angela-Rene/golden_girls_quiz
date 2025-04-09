take_again = True
while True:


    print("-------------------------------------\nWhich Golden Girls character are you?\n--------------------------------------")
    print("Are you a Dorothy, Rose, Blanche, or Sophia? \nTake this quiz to find out!!\n--------------------------------------")

    print("Please answer the following questions with A, B, C, or D\n-----------------------------------")

    answer1 = str(input("1. First, where would you like to live?\n  A- New York City.\n  B- On a farm, with plenty of snow.\n  C- A big, fancy house in the south.\n  D- Anywhere but the retirement home!\n")).upper()
    if answer1 == "A":
        answer1 = "Dorothy"
    elif answer1 == "B":
        answer1 = "Rose"
    elif answer1 == "C":
        answer1 = "Blanche"
    elif answer1 == "D":
        answer1 = "Sophia"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("----------------------------------")

    answer2 = str(input("2. Which job would you prefer?\n  A- cooking delicious food\n  B- a grief counselor\n  C- teaching children\n  D- assistant in an art museum\n")).upper()
    if answer2 == "A":
        answer2 = "Sophia"
    elif answer2 == "B":
        answer2 = "Rose"
    elif answer2 == "C":
        answer2 = "Dorothy"
    elif answer2 == "D":
        answer2 = "Blanche"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("---------------------------------")

    answer3 = str(input("3. What is your favorite thing to drink?\n  A) milk\n  B) scotch\n  C) margarita\n  D) wine\n")).upper()
    if answer3 == "A":
        answer3 = "Rose"
    elif answer3 == "B":
        answer3 = "Dorothy"
    elif answer3 == "C":
        answer3 = "Blanche"
    elif answer3 == "D":
        answer3= "Sophia"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("---------------------------------")


    answer4 = str(input("4. Other than cheesecake, what is your favorite food?\n  A) Lasagna \n  B) Cookies with tea\n  C) No cheesecake? Then cheeseballs!\n  D) I find it ridiculous that cheesecake is not an option.\n")).upper()
    if answer4 == "A":
        answer4 = "Sophia"
    elif answer4 == "B":
        answer4 = "Blanche"
    elif answer4 == "C":
        answer4 = "Rose"
    elif answer4 == "D":
        answer4 = "Dorothy"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("---------------------------------")

    answer5 = str(input("5. You're going out for errands, and maybe some lunch. What outfit do you wear?\n  A) Something down-home and practical\n  B) A tailored, pulled together look\n  C) Something soft, sexy, and flowing\n  D) Comfort over everything else\n")).upper()
    if answer5 == "A":
        answer5 = "Rose"
    elif answer5 == "B":
        answer5 = "Dorothy"
    elif answer5 == "C":
        answer5 = "Blanche"
    elif answer5 == "D":
        answer5 = "Sophia"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("--------------------------------")

    answer6 = str(input("6. What color is that outfit?\n  A) Navy blue\n  B) Emerald green\n  C) Vibrant yellow\n  D) Classic black\n")).upper()
    if answer6 == "A":
        answer6 = "Dorothy"
    elif answer6 == "B":
        answer6 = "Blanche"
    elif answer6 == "C":
        answer6 = "Rose"
    elif answer6 == "D":
        answer6 = "Sophia"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("----------------------------------")

    answer7 = str(input("7. And finally, your friend needs some advice about an important decision. You respond by:\n  A) Telling them a humurous story from your past, whether or not it is relevant.\n  B) Giving them practical advice, since you are obviously the voice of reason.\n  C) Telling an outrageous, made-up story to make sure your point gets accross.\n  D) Talking about your own problem that is clearly more important.\n")).upper()
    if answer7 == "A":
        answer7 = "Rose"
    elif answer7 == "B":
        answer7 = "Dorothy"
    elif answer7 == "C":
        answer7 = "Sophia"
    elif answer7 == "D":
        answer7 = "Blanche"
    else:
        print("Please choose 'A', 'B', 'C', or 'D'")
    print("---------------------------------")



    print("The results are in!")

    golden_girls_dict = {"Dorothy": 0, "Rose": 0, "Blanche": 0, "Sophia": 0}
    answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7 ]

    for answer in answers:
        golden_girls_dict[answer] += 1
        
    most_frequent = max(golden_girls_dict, key = golden_girls_dict.get)

    if most_frequent == "Sophia":
        print("You are a Sophia!\nYour quick-witted staight talk is as sharp as your recipes are delicious!  You've seen a lot, and don't put up with nonsense. Good for you!")
    elif most_frequent == "Blanche":
        print("You are a Blanche!\nYou're the southern belle type. And though you can be self-absorbed, you are confident and fearless to go after what you want!")
    elif most_frequent == "Rose":
        print("You are a Rose!\nYou are sweet, kind, and a bit naive.  But you have the best stories! Keep spreading all the sunshine!")
    elif most_frequent == "Dorothy":
        print("You are a Dorothy!\nYou are quick-witted, short-tempered, and very practical. Keep being the loyal friend that makes sure stuff gets done!")
        
        
    take_again = input("Would you like to take the quiz again? (Y/N)").lower()
    if take_again == "n":
        print("Thanks for playing!")
        break
    elif take_again == "y":
        continue
    else:
        break
    