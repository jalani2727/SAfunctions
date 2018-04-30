star = "*" 
line = ""
while len(line) <5:
    line = line + star
y = 0
while y < 5:
    print(line)
    y+= 1

"""
#another way

size = 5 
count_x = 0
count_y = 0

while count_y < size:
    while count_x < size:
        print('*' , end='')
        count_x += 1

    count_y += 1
    print()
"""

def makeSquare():
    star = "*" 
    line = ""
    while len(line) <5:
        line = line + star
    y = 0
    while y < 5:
        print(line)
        y+= 1


        