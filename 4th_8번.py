# 사용자가 입력하는 3개의 좌표 (x,y)를 리스트에 저장한다 이들 좌표를 꺼내서 거북이를 이동하는 프로그램을 작성해보자.
import turtle
t = turtle.Turtle()
t.shape("turtle")

x = []
y = []

x1 = int(input("x1:"))
x.append(x1)
y1 = int(input("y1:"))
y.append(y1)

x2 = int(input("x2:"))
x.append(x2)
y2 = int(input("y2:"))
y.append(y2)

x3 = int(input("x3:"))
x.append(x3)
y3 = int(input("y3:"))
y.append(y3)

t.goto(x[0], y[0])
t.goto(x[1], y[1])
t.goto(x[2], y[2])

t._screen.exitonclick()  # 마우스로 클릭을 해야 화면이 종료됨
