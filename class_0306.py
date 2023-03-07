# def func1():
#     global a # global 지역변수를 전역 변수로 사용 할 때
#     a = 1222
#     print("func1의 a : %d"%a)

# def func2():
#     print("func2의 a : %d"%a)
# a=200 #전역 변수
# func1()
# func2()

# def sum_func(x1,x2,x3 = 100):
#     result=0
#     result=x1+x2+x3
#     return result
# def display():
#     Sum=0
#     a,b,c=10,20,30
#     Sum=sum_func(a,b)
#     print("매개변수 2개 함수 호출 : ",Sum)
#     Sum = sum_func(a,b,c)
#     print("매개변수 3개 함수 호출 : ",Sum)
# display()

# def alba(day=30,time=8,won=8500): # 기본 매개변수는 맨 오른쪽부터 배치한다.
#     result=day*time*won
#     return result
# def display():
#     num=int(input("1.기본급\n2.일한 날짜 입력\n"))
#     if num==1:
#         result=alba()
#     elif num==2:
#         day=int(input('일한 날짜 입력(몇일) : '))
#         result=alba(day)
#     print("당신의 급여 : {}원 입니다.".format(result))
# display()

# def sum_func(*par):
#     result=0
#     print("type : ",type(par))
#     print("par : ",par)
#     for num in par:
#         result=result+num
#         print("num : %d"%num)
#     return result
# Sum=0
# Sum=sum_func(10,20)
# print("매개변수 2개 함수 : %d"% Sum)
# Sum=sum_func(10,20,30,40)
# print("매개변수 4개 함수 : %d"% Sum)

# def dic_func(**par):
#     print("type(par) : ",type(par))
#     print(par)
#     for k in par.keys():
#         print("{} : {}명입니다".format(k, par[k]))

# dic_func(똭뚝뽹=123, 꿔익꿔익=8, test='테스뚜')

# def change(a,b,c):
#     return a+10,b+20,c+30

# a,b,c=change(10,20,30)
# d=change(10,20,30)
# print("a,b,c : ",a,b,c)
# print("d:{}, type{}".format(d,type(d)))

# def swap(x,y):
#     return y,x

# a=10; b=20
# print("바꾸기 전 : ",a,b)
# a,b=swap(a,b)
# print("바꾼 후 : ",a,b)

# swap=lambda a,b:[b,a] # 함수명=lambda함수 a,b:[b:a] 짧고 간단하게 한 줄이면서 일회성일 경우 사용
# a=swap(10,20)
# print("swap 결과",a)

# lam = lambda a:a*10
# hap = lambda a,b:a+b
# noData = lambda : print("인자값 없는 람다")

# print(lam(10))
# print(hap(5,10))
# noData()

# def startGame():
#     print("Game Start!!!!")
# def test():
#     print("1.게임 시작")
#     print("2.게임 종료")
#     num=input("선택 : ")
#     if num=="1":
#         startGame()
#     elif num=="2":
#         end()
# end=lambda :print("게임 종료")
# test()

# sum=lambda a,b:a+b
# sub=lambda a,b:a-b
# mul=lambda a,b:a*b
# div=lambda a,b:a/b
# print("sum : ",sum(10,20))
# print("sub : ",sub(10,20))
# print("mul : ",mul(10,20))
# print("div : ",div(10,20))

# def transfer(dst,su=0,won=500):
#     for i in range(0,su):
#         won*=2
#     return"{}까지 요금 : {}입니다".format(dst,won)
# def disply():
#     destination=''; su=0
#     num=int(input('1.환승 안함\n2.환승 함\n3.장거리\n'))
#     destination=input('목적지 입력 : ')
#     if num==1:
#         result=transfer(destination)
#     elif num==2:
#         su=int(input('환승 수 입력 : '))
#         result=transfer(destination,su)
#     else:
#         result=transfer(destination,1,10000)
#     print(result)
# disply()

# 모듈

# import math

# print(math.pi)
# print(math.factorial(5)) # 5!=5x4x3x2x1
# print(math.sqrt(5))
# print(math.log10(2))

# from math import factorial, sqrt, pi

# print(factorial(5))
# print(sqrt(5))
# print(log10(2))

# from math import factorial, sqrt, pi
# import math

# print(factorial(5))
# print(sqrt(5))
# print(math.log10(2))
# print(math.log10(3))
# print(math.gcd(12,18)) # 최대공약수

# import statistics

# points=[65,75,55]
# print('평균 : ',statistics.mean(points))
# print('분산 : ',statistics.variance(points))
# print('표준편차 : ',statistics.stdev(points))
# #-------------------------------------------------------
# import statistics as st # 모듈명 줄일 수 있음

# points=[65,75,55]
# print('평균 : ',st.mean(points))
# print('분산 : ',st.variance(points))
# print('표준편차 : ',st.stdev(points))

# import _8calculator as cal # 모듈명 공백, 첫번째자리 숫자 사용 불가능
# from _8calculator import info

# print("1인치 : %.2fcm"%cal.inch)
# print("1~10까지의 누적합:",cal.calc_sum(10))

# info()
# info()
# info()

# import random

# i=0
# for i in range(5):
#     print(i,"",random.random())

# import random
# i=0
# for i in range(5):
#     print(i,"",int(random.random()*100))

# import random
# i=0
# for i in range(5):
#     print(i,"",random.randrange(1,10))

# n1=10
# n2=0
# try:
#     result=n1/n2
#     print("%d/%d=%d"%(n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다.")
# print("프로그램 정상 종료!!")

# while True:
#     try :
#         n1=int(input('정수1 : '))
#         n2=int(input('정수2 : '))
#         break
#     except:
#         print("숫자로만 입력하세요~")
#     # print('%d/%d=%d'%(n1,n2,result))
# try:
#     result=n1/n2
#     print('%d/%d=%d'%(n1,n2,result))
# except:
#     print('0으로 나눌 수 없습니다.')
# print('프로그램 정상 종료!!')

# s=input('정수 : ')
# try:
#     point=int(s)
#     print(150/point)
# except ValueError:
#     print('숫자로만 입력하세요~')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except:
#     print('알 수 없는 오류 발생. 점검 후 조치하겠습니다..')
# print('프로그램 정상 종료!')

# pet=['거북이','타란튤라','전갈']
# for i in range(4):
#     try:
#         print(pet[i],'키울래용!')
#     except:
#         print('애완동물의 정보가 없습니다.')
#     finally:# 예외처리(에러)와 상관없이 꼭 실행되어야 하는 경우
#         print('애완동물 넘 조아~~')
# print('프로그램 정상 종료!')

# 가위바위보
# import random

# a1=int(input('가위바위보 게임\n0.가위 1.바위 2.보\n>'))
# a=random.randrange(0,3)
# b=["가위","바위","보"]

# print("사용자 :",b[a1],'\n',"컴퓨터 :",b[a])
# if a1==a:
#     print('무승부')
# elif a-a1==-1 or a-a1==2:
#     print('승리')
# else:
#     print('패배')

# 로또
import random
lotto=[]; num=0
result=True
print("===로또 추첨===")
while result:
    num=random.randrange(1,46)
    if lotto.count(num)==0:
       lotto.append(num)
    if len(lotto)>=6:
        result=False
else:
    print("추첨된 번호" , end="\n")
    lotto.sort()
for i in range(0,len(lotto)):
    print("{}".format(lotto[i],end=""))

import random
lotto=[]; num=0
result=True
print("===로또 추첨===")
while result:
    num=random.randrange(1,46)
    if lotto.count(num)==0:
       lotto.append(num)
    if len(lotto)>=6:
        result=False
else:
    print("추첨된 번호" , end="\n")
    lotto.sort()
for i in range(0,len(lotto)):
    print("{}".format(lotto[i],end=""))

import random
lotto=[]; num=0
result=True
print("===로또 추첨===")
while result:
    num=random.randrange(1,46)
    if lotto.count(num)==0:
       lotto.append(num)
    if len(lotto)>=6:
        result=False
else:
    print("추첨된 번호" , end="\n")
    lotto.sort()
for i in range(0,len(lotto)):
    print("{}".format(lotto[i],end=""))

import random
lotto=[]; num=0
result=True
print("===로또 추첨===")
while result:
    num=random.randrange(1,46)
    if lotto.count(num)==0:
       lotto.append(num)
    if len(lotto)>=6:
        result=False
else:
    print("추첨된 번호" , end="\n")
    lotto.sort()
for i in range(0,len(lotto)):
    print("{}".format(lotto[i],end=""))

import random
lotto=[]; num=0
result=True
print("===로또 추첨===")
while result:
    num=random.randrange(1,46)
    if lotto.count(num)==0:
       lotto.append(num)
    if len(lotto)>=6:
        result=False
else:
    print("추첨된 번호" , end="\n")
    lotto.sort()
for i in range(0,len(lotto)):
    print("{}".format(lotto[i],end=""))