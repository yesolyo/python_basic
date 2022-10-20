import turtle

color_list=["blue","green","black","red"]
count=0
turtle.setup(width=500, height=500)
t=turtle.Pen()
t.width(3)
t.speed(3)
for i in range(0,301,10):
    t.forward(i)
    t.pencolor(color_list[count%4])
    t.left(120)
    count +=1
