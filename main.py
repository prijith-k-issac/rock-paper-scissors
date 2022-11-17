import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
icon = [rock,paper,scissors]
#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.   "))
system_choice =random.randint(0,2)


# rock=0,paper=1,scissor=2
# logic --->(system_choice,user_choice,result)
# (0,0,draw),(0,1,user),(0,2,system)-->here system_choice=0(rock)-->so i naming this sequence as system_choice_rock
# (1,0,system),(1,1,draw),(1,2,user)-->here system_choice=1(paper)so i naming this sequence as system_choice_paper
# (2,0,user),(2,1,system),(2,2,draw)-->here system_choice=2(scissor)so i naming this sequence as system_choice_scissor,from this I making a result lists
system_choice_rock =['draw','user','system']
system_choice_paper =['system','draw','user']
system_choice_scissor =['user','system','draw']

if user_choice == 0 or user_choice == 1 or user_choice == 2:
  # comparing the choices
  if system_choice==0:
    result= system_choice_rock[user_choice]
  
  elif system_choice==1:
    result= system_choice_paper[user_choice]

  elif system_choice==2:
    result= system_choice_scissor[user_choice] 
  print("\nYou opted",icon[user_choice])
  print("\nSystem opted",icon[system_choice])
# checking result
  if result =='draw':
    print("Draw")
  elif result =='user':  
    print("You won the match")
  else:
    print("You lose the match")

else:
    print("Invalid Entry")

  

