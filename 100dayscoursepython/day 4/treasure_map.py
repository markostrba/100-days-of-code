          #A    #B   #C
line1 = ["⬜️","️⬜️","️⬜️"]#1
line2 = ["⬜️","⬜️","️⬜️"]#2
line3 = ["⬜️️","⬜️️","⬜️️"]#3
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().lower()
if position[0] == 'a':
    vertical_position = int(position[1])-1
    treasure = (map[vertical_position])[0] = 'X'
elif position[0] == 'b':
    vertical_position = int(position[1])-1
    treasure = (map[vertical_position])[1] = 'X'
elif position[0] == 'c':
    vertical_position = int(position[1])-1
    treasure = (map[vertical_position])[2] = 'X' 

print(f"{line1}\n{line2}\n{line3}")