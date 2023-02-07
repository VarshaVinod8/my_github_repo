import random

def display(room):
    print(room)

room = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print("All rooms are dirty")
display(room)

x=0
y=0

while x<4:
    while y<4:
        room[x][y]= random.choice([0,1])
        y+=1
    x+=1

display(room)
x=0
y=0
z=0
while x<4:
    while y<4:
        if room[x][y] == 1:
            print("loacation dirty ", x,y)
            room[x][y] = 0
            print("cleaned ", x , y)
            z+=1
        y+=1
    x+=1
    y=0

perf = (100 - ((z/16) *100))
print("all rooms are clean")
display(room)
print("performance ", perf)