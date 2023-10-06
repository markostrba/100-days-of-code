name1 = input('name: ')
name2 = input('name: ')
combined_names = name1 + name2
lower_names = combined_names.lower()

t_letter =lower_names.count('t')
r_letter =lower_names.count('r')
u_letter =lower_names.count('u')
e_letter =lower_names.count('e')
first_digit = t_letter + r_letter + u_letter + e_letter

l_letter = lower_names.count('l')
o_letter = lower_names.count('o')
v_letter = lower_names.count('v')
e_letter = lower_names.count('e')
second_digit = l_letter + o_letter + v_letter + e_letter
score = int(str(first_digit) + str(second_digit))
if score < 9 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos')
elif score >= 40 and score <= 50:
    print(f'your score is {score} you are alright together')
else:
    print(f'Your score is {score}')