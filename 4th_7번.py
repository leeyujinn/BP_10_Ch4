# 사용자가 입력하는 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그 색상으로 채워진 원을 그리는 프로그램을 작성해보자. 반복문은 사용하지 않는다. 채워진 원을 그리면 다음과 같은 문장들을 사용한다.
import turtle  # turtle 라이브러리를 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 불러오기

color = []  # color 리스트

color1 = input("색상 #1을 입력하시오:")  # 사용자로부터 색상 #1을 입력받음
color.append(color1)  # 변수 color 리스트에 color1의 값을 추가함
color2 = input("색상 #2를 입력하시오:")  # 사용자로부터 색상 #2을 입력받음
color.append(color2)  # 변수 color 리스트에 color2의 값을 추가함
color3 = input("색상 #3을 입력하시오:")  # 사용자로부터 색상 #3을 입력받음
color.append(color3)  # 변수 color 리스트에 color3의 값을 추가함

t.fillcolor(color[2])  # color3의 색을 채움
t.begin_fill()  # 채우기를 시작
t.circle(50)  # 반지름이 50인 원을 그림
t.end_fill()  # 채우기를 종료
t.penup()  # 그리기 모드 시작
t.goto(100, 0)  # (100,0)점으로 이동
t.pendown()  # 그리기 모드 종료

t.fillcolor(color[1])  # color2의 색을 채움
t.begin_fill()  # 채우기를 시작
t.circle(50)  # 반지름이 50인 원을 그림
t.end_fill()  # 채우기를 종료
t.penup()  # 그리기 모드 시작
t.goto(200, 0)  # (200,0)점으로 이동
t.pendown()  # 그리기 모드 종료

t.fillcolor(color[0])  # color1의 색을 채움
t.begin_fill()  # 채우기를 시작
t.circle(50)  # 반지름이 50인 원을 그림
t.end_fill()  # 채우기를 종료

t._screen.exitonclick()  # 마우스로 클릭을 해야 화면이 종료됨
