import random 

name_list = ['Angela','Ben','Jenny','Michael','Chloe']
num_items = len(name_list)
random_choice = random.randint(0,num_items -1 )
random_name = name_list[random_choice]
print(random_name)