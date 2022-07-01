    
import quizQuestions  

score = 0
#  functionn to do math
def playAgain():
    play_again = input("Do you want to play again ? (y/n) ")
    if play_again =="y":
        global score
        score = 0
        play()
    else: 
        end()
     
def result(ans,UserAnswer):
    global score 
    
    if ans == UserAnswer:
        print("That's the correct answer!")
        score = score +1
    
    else :
        print("Unfortunately, that is not the correct answer")
        
    print(f"Score : {score}")
    
def compliment():
    if score <= 2:
        print("You need to work hard, try again!")
        
    elif score <= 4 :
        print("That's good, not bad not bad")
        
    else:
        print("Bravo ! That's remarkable")
        
        
def Fresult(ans,UserAnswer):
      if ans == UserAnswer:
            print("That's correct! You won")
            global score 
            score = score +1
    
      else :
        print("Unfortunately, that is not the correct answer")
        
      print(f"Final score : {score}")
      
    #   giving feedback and compliment to the user
      compliment()
  
           
def play():
  
    # do this by making a function
    # Question no. 1
    
    print(f"{quizQuestions.questions[0]} \n")
    answer = input("Your answer : ")
    result("a",answer)
  
    
    # Question no. 2 
    print(f"{quizQuestions.questions[1]}")
    answer = input("Your answer : ")
    result("d",answer)

    
      
    # Question no. 3 
    print(f"{quizQuestions.questions[2]}")
    answer = input("Your answer : ")
    result("c",answer)

    
      
    # Question no. 4 
    print(f"{quizQuestions.questions[3]}")
    answer = input("Your answer : ")
    result("b",answer)

    
    
      
    # Question no. 5
    print(f"{quizQuestions.questions[4]}")
    answer = input("Your answer : ")
    Fresult("d",answer)

   
#    If user want to play again
    playAgain()
    
def end():
    print("Ok goodnight you are going to miss such a fun")   
def main():
   
        
    decision = input("Do you want to play the game ?(y/n) ")
    if decision == "y": 
        
        play()
        
    else: 
        end()
        
main()