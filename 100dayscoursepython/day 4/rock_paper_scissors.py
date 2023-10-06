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
list_options = rock,paper,scissors
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
user_choice_list_options = list_options[user_choice]
print(user_choice_list_options)
computer_choice = random.randint(1,3)-1
comp_choice_list_options= list_options[computer_choice]
print(f'Computer chose:\n{comp_choice_list_options}')
if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print('You Win!')
elif (user_choice == 2 and computer_choice == 0) or (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2):
    print('You lose!')
else:
    print('Draw!')
