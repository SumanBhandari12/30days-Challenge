# Importing the quiz questions
import quizQuestions


# Creating the class
class Quiz:
    
    # constructor function
    def __init__(self):
        self.score = 0
        
    def main(self):
        decision = input("Do you want to play the game ?(y/n) ")
        
        if decision == "y": 
            self.play()
        else: 
            self.end()
            
    def play(self):
        
         # Question no. 1
            print(f"{quizQuestions.questions[0]} \n")
            answer = input("Your answer : ")
            self.result("a",answer)
        
            
            # Question no. 2 
            print(f"{quizQuestions.questions[1]}")
            answer = input("Your answer : ")
            self.result("d",answer)

            
            
            # Question no. 3 
            print(f"{quizQuestions.questions[2]}")
            answer = input("Your answer : ")
            self.result("c",answer)

            
            
            # Question no. 4 
            print(f"{quizQuestions.questions[3]}")
            answer = input("Your answer : ")
            self.result("b",answer)

            
            
            
            # Question no. 5
            print(f"{quizQuestions.questions[4]}")
            answer = input("Your answer : ")
            self.Fresult("d",answer)
            
    #    If user want to play again
            self.playAgain()
                  
    def end(self):
        print("Ok goodnight you are going to miss such a fun")  
        
    def result(self,ans,UserAnswer):
    
        if ans == UserAnswer:
            print("That's the correct answer!")
            self.score = self.score +1
        
        else :
            print("Unfortunately, that is not the correct answer")
            
        print(f"Score : {self.score}")
    
            
    def Fresult(self,ans,UserAnswer):
        if ans == UserAnswer:
                print("That's correct! You won")
                self.score = self.score +1
        
        else :
            print("Unfortunately, that is not the correct answer")
            
        print(f"Final score : {self.score}")
        
        #   giving feedback and compliment to the user
        self.compliment()
      
    def compliment(self):
        if self.score <= 2:
            print("You need to work hard, try again!")
            
        elif self.score <= 4 :
            print("That's good, not bad not bad")
            
        else:
            print("Bravo ! That's remarkable")
    
    
    def playAgain(self):
        play_again = input("Do you want to play again ? (y/n) ")
        if play_again =="y":
            self.score = 0
            self.play()
        else: 
            self.end()
    
quiz = Quiz()
quiz.main()