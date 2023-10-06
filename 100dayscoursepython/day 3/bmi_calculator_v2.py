height = float(input())
weight  = int(input())

bmi_calculator = weight/(height*height)
if bmi_calculator < 18.5:
    print(f'{bmi_calculator} underweight')
elif bmi_calculator < 25:
    print(f'{bmi_calculator} normal weight')
elif bmi_calculator < 30:
    print(f'{bmi_calculator} slightly overweight')
elif bmi_calculator < 35:
    print(f'{bmi_calculator} obese')
else:
    print(f'{bmi_calculator} clinical obese')
