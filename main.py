#project
from turtle import *
speed(400)
left(90)
up()
backward(50)
down()
bgcolor('black')
def branch(a):
    if a < 10:

        color('green')
        stamp()
        color('brown')
        return
    else:
        color('brown')
        pensize(3)
        forward(a)
        left(30)
        branch(a * 3/4)
        right(60)
        branch(a * 3/4)
        left(30)
        backward(a)

#print(branch(100))
exitonclick()



a1 = [0]
IN_NUM = int(input('Введите количество колец: '))
a = a1 * IN_NUM
b = []
c = []

#point1(нач точка),point2(кон точка)
def hanoy(point1,point2):
    print('Из стержня ',point1, ' в стержень ', point2)


def hanoytower (IN_NUM, point1, point2, temp):
    if IN_NUM == 0:
        return
    #Из начальной точки во вспомогательную
    hanoytower(IN_NUM-1, point1, temp, point2)
    hanoy(point1,point2)
    #из Вспомогательной (temp) в конечную
    hanoytower(IN_NUM-1, temp, point2, point1)


def print_hanoy(IN_NUM, a, b, c):
    if IN_NUM == 0:
        print('Получилось:')
        return True
    a.pop(0)
    c.append(0)
    print('A: ', a)
    print('B: ', b)
    print('C: ', c)
    c.pop(0)
    b.append(0)
    print_hanoy(IN_NUM-1, a, b, c)
    if len(b) == IN_NUM:
        print('A: ', a)
        print('B: ', b)
        print('C: ', c)


def main():
    print(hanoytower(IN_NUM,'a','b','c'))
    print('Ход решения:')
    print('A: ', a)
    print('B: ', b)
    print('C: ', c)
    print(print_hanoy(IN_NUM,a,b,c))
main()