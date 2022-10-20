import easygui
import turtle

lang=easygui.buttonbox("모양을 선택하세요",choices=['circle','rectangle'])
guess=int(easygui.enterbox("개수를 입력하세요"))
turtle.setup(width=800, height=800)
t=turtle.Pen()
t.speed(5)
if lang=='rectangle':
    for i in range(guess):
        for i in range(4):
            t.forward(50)
            t.right(90)
        t.up()
        t.forward(50)
        t.down()


elif lang=='circle':
    for i in range(guess):
        t.circle(20)
        t.up()
        t.forward(40)
        t.down()
