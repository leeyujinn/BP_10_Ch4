# 사용자가 입력하는 3개의 좌표 (x,y)를 리스트에 저장한다 이들 좌표를 꺼내서 거북이를 이동하는 프로그램을 작성해보자.
import turtle # turtle 라이브러리를 불러오기
t = turtle.Turtle() #변수 t에 turtle.Turtle()를 선언
t.shape("turtle") #turtle 도형 불러오기

x = [] #변수 x의 리스트
y = [] #변수 y의 리스트

x1 = int(input("x1:")) #사용자로부터 x1의 값을 받음
x.append(x1) #변수 x의 리스트에 x1의 값을 추가함
y1 = int(input("y1:")) #사용자로부터 y1의 값을 받음
y.append(y1) #변수 y의 리스트에 y1의 값을 추가함

x2 = int(input("x2:")) #사용자로 부터 x2의 값을 받음
x.append(x2) #변수 x의 리스트에 x2의 값을 추가함
y2 = int(input("y2:")) #사용자로부터 y2의 값을 받음
y.append(y2) #변수 y의 리스트에 y2의 값을 추가함

x3 = int(input("x3:")) #사용자로부터 x3의 값을 받음
x.append(x3) #변수 x의 리스트에 x3의 값을 추가함
y3 = int(input("y3:")) #사용자로부터 y3의 값을 받음
y.append(y3) #변수 y의 리스트에 y3의 값을 추가함

t.goto(x[0], y[0]) #(x1,y1)로 이동
t.goto(x[1], y[1]) #(x2,y2)로 이동
t.goto(x[2], y[2]) #(x3,y3)으로 이동

t._screen.exitonclick()  # 마우스로 클릭을 해야 화면이 종료됨
