import random
#from secrets import choice
 #Am going to print out the game rules and instructions
print("winning  rules of the game : \n"        
       +"rock vs paper    --> paper wins\n" 
       +"rock vs scissor  --> rock wins\n" 
       +"paper vs scissor --> scossor wins\n")
 #display the choices in terms if integers
while True:
     print("Enter choice : \n 1) for rock, \n 2) for paper, and \n 3) for scissor")
     #enter your choice
     choice = int(input("enter your choice: "))
     #check if the input is valid
     while choice > 3 or choice < 1 :
         choice = int(input("enter valid input my guy! : "))
     #loop through giving each instance 
     if choice == 1:
        choice_name ='rock'
     elif choice == 2:
         choice_name ='paper'
     else:
         choice_name = 'scissor'
     #print users output
     print("your valid input was :" +choice_name)
    
     #computer choice play
     print("comps turn to play")
    
     #inbuild function intance
     comp_choice=random.randint(1,3)
     #equal variables comp choice, choice
     while comp_choice == choice:
         comp_choice=random.randint(1,3)
         #loop through 
         if comp_choice == 1:
            comp_choice_name ='rock'
         elif comp_choice == 2:
             comp_choice_name = 'paper'
         else:
             comp_choice_name ='scissor'
            
         #print comp choice
         print("comp choice: " +comp_choice_name)
    
     #condition for winning
     if((choice_name == 1 and comp_choice_name ==2) or (choice_name==2 and comp_choice_name==1)):
         print("paper wins =>", end="")
         result = "paper"
     elif((choice_name==1 and comp_choice_name==3)or(choice_name==3 and comp_choice_name == 1)):
         print("rock wins =>",end ="")
         result = "rock"
     else:
         print("scissor wins =>", end="")
         result="scissor"
        
     #condition for user or comp winning
     if result==choice_name :
         print("user wins")
     else:
         print("comp wins")
        
     #option to continue or quit
     print("do you wanna play again : enter Y/N")
     answer = input()
     if answer =='N'or answer=='n':
        break
     
     
#for i in range(0, 10):
   # print(1,2,3, sep=",")