#Манцеров Платон ИИ-71
#Уровень С (сложный)
#№1
import random
def sum_odd():
    global lst
    sum = 0
    lst = [random.randint(1,20) for i in range(random.randint(1, 20))]#я сделал т.к. постоянно изменять список вручную слишком долго
    print(lst)
    for i in range(0, len(lst)-1):
        if lst[i] % 2 != 0:
            sum = sum + lst[i]
            lst.pop(i)
            lst.insert(i,sum)
    lst.append(sum)
    print(lst)
sum_odd()


#№2
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
print(distance(int(input()),int(input()),int(input()),int(input())))

def triamgle_perimetr(x1,y1,x2,y2,x3,y3):
    s1=distance(x1,y1,x2,y2)
    s2=distance(x2,y2,x3,y3)
    s3=distance(x3,y3,x1,y1)
    return s1+s2+s3
print(triamgle_perimetr(int(input()),int(input()),int(input()),int(input()),int(input()),int(input())))


#№3
num = int(input())
lst = 1
result = ""
def check(num, lst):
    global result
    if lst > num:
        result = "NO"
    else:
        if lst == num:
            result = "YES"
        else:
            lst *= 2
            check(num, lst)

check(num, lst)
print(result)
