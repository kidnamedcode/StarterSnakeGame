score = 0
print("Untitled geo game: guess capital cities of different countries")
questions = [
    ["What is the capital of Australia","Canberra"],
    ["What is the capital of New Zealand","Wellington"],
    ["What is the capital of Finland","Helsinki"]
]
for question, correctanswer in questions:
    answer = input(question)
    print("Your answer is..."+answer.strip().lower(),"The correct answer is:"+ correctanswer)
    if answer.strip().lower() == correctanswer.strip().lower():
        print("Correct")
        score = score + 1
    elif score > 0:
        print("no")
        score = score -1
print(f"your current score is {score}, lets try Australian states now:")
questions = [
    ["What is the capital of New South Wales","Sydney"],
    ["What is the capital of Queensland","Brisbane"],
    ["What is the capital of Tasmania","Launceston"]
]
for question, correctanswer in questions:
    answer = input(question)
    print("Your answer is..."+answer.strip().lower(),"The correct answer is:"+ correctanswer)
    if answer.strip().lower() == correctanswer.strip().lower():
        print("Correct")
        score = score + 1
    elif score > 0:
        print("no")
        score = score -1
print(f"Your score now is... {score}")
if score == 6:
    print("A full score of 6/6! Great")
else:print("Keep trying, I'm sure you'll get them all right next time")


