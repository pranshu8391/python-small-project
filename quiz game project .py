
#the quiz game project 


print("welcome to the quiz game")

score=0                                                               #variable 

answer=input("what is the captal of india? ")                         # frist question 

if answer. lower() == "new delhi":
    score += 1                              


    answer=input("who is the frist prime minister of india? ")         #second question

    if answer.lower() == "pandit jawahar neharu":
        score += 1

        answer = input("what is the capital of maharastra? ")         # third question 

        if answer.lower() == "mumbai":
            score +=1


            print(f"your finale score{score}/3")                      # finale answer

    


