width = input('Width?: ')
height = input('Height?: ')
star = "*" 
line = ""
while len(line) < int(width):
    line = line + star
print(line)
line2 = (" ") * int(width)
line3 = star + line2[0:(int(width)-2)] + star
x = 0
while x < (int(height) -2):
    x += 1
    print(line2)
    print(line3)
print(line2)
print(line)    

