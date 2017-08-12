score = float(input("Enter your score "))

if score >100:
    print(score,"is invalid score.")
elif score >= 90:
    print("Your score is AA with",score)
elif score >=85:
    print("Your score is AB with",score)
elif score >=80:
    print("Your score is BB with",score)
elif score >=70:
    print("Your score is BC with",score)
else:
    print("You did not pass the class with",score)