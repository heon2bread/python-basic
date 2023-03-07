# floor1=260
# floors=14
# # firstfl=5.0023
# firstfl=500.23
# hotel=firstfl+(floors-1)*floor1
# meter=hotel/100
# print('건물의 총 높이(m) :', round(meter,3),'%c'% 'm')

# onem=100/11.27
# onehour=onem*3600
# km=onehour/1000
# print('1시간 동안 갈 수 있는 거리(km) :',round(km,2),'km')

# flt = 123.123
# print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321))
# print(flt,"+",321.321,"=",flt+321.321)

# ch1,ch2,ch3="파",'2','썬'
# print("%c + %c + %c = %s" %(ch1,ch2,ch3,ch1+ch2+ch3))
# print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3)

# str_1="python"; str_2="test"
# str_3=str_1 + str_2
# print("%s + %s = %s" % (str_1,str_2,str_1+str_2))
# print(str_1,"+",str_2,"+",str_1+str_2)

# +연산자의 연산
# 숫자(정수,실수) + 숫자(정수,실수)는 우리가 흔히 아는 덧셈을 진행
# 시퀀스형 자료형의 + 연산은 하나로 합치는 업데이트 연산이 진행
# 시퀀스형 자료형 (리스트, 튜플, 문자열)
# -> 순서가 존재하며, 인덱스라는 보조첨자를 사용하는 것이 특징
# 단, 좌우의 피연산자의 속성이 같아야 한다.
# 리스트 + 리스트
# 튜플 + 튜플
# 문자열 + 문자열
# 예) 문자열 + 정수 는 연산이 불가능함.

# A=10
# B=5
# print("type :",type(A<B));print("type:",(A<B))
# num=100;print("type : %s" %  type(num))
# flt=321.321;print("type : %s" % type(flt))
# ch="A";print("type : %s" % type(ch))
# st="test";print("type : %s" % type(st))

# num=100
# print("type : %s\tid : %s" % (type(num),id(num)))
# num=321.321
# print("type : %s\tid : %s" % (type(num),id(num)))
# num="A"
# print("type : %s\tid : %s" % (type(num),id(num)))
# num="test"
# print("type : %s\tid : %s" % (type(num),id(num)))

# st1 ="Python"
# st2 ="Test"
# su =100
# flt =1.11

# num ='100'

# print(flt+su)
# print(st1 + st2)
# print(su+num)

# typeerror - 변수, 자료형 에러

# su = 100
# str(su)
# int(su)
# su =str(su)
# print('type(su):', type(su))
# print('type(str(su)):', type(str(su)))
# print('type(float(su)):', type(float(su)))
# print(type(su))

# 모든 데이터는 문자열로 변형 가능
# 정수는 실수로 변환 가능 
# 실수는 정수로 변환 불가

# su=100
# num='100'
# flt="1.111"
# # print(type(int(num)), su+num)
# print(su+int(num))
# print(su+float(flt))
# print(str(su)+num)

# 상세 안내 필요
# print("숫자 입력")
# num1=input()
# print("입력 받은 값 : ", num1)

# print('이름 입력')
# name=input()
# print("나이 입력")
# age=input()
# print(name,"님의 나이는",age,"살 입니다.")

# print("두 수의 합을 구해 줍니다")
# print("두 수 입력")

# num1=input()
# num2=input()
# num3=int(num1) + int(num2)
# print("두 수의 합", num1,"+",num2,'=',num3)

# print("num1 type : ", type(num1))
# print("num2 type : ", type(num2))
# print("num3 type : ", type(num3))

# print("두 수 입력")
# num1 = int(input())
# num2 = int(input())

# result = num1 + num2
# print(num1,"+",num2,"=",result)

# result = num1 - num2
# print(num1,"-",num2,"=",result)

# result = num1 * num2
# print(num1,"*",num2,"=",result)

# result = num1 / num2
# print(num1,"/",num2,"=", (result))

# print('문자열 입력')
# name = input()
# print('정수 입력')
# age = int(input())
# print('실수 입력')
# flt = float(input())

# print('name 값 : ',name,'\t type : ', type(name))
# print('age 값 : ',age,'\t type : ', type(age))
# print('flt 값 : ',flt,'\t type : ', type(flt))

# name = input("이름을 입력 하세요 : ")
# # name = input("문자를","두개""이상은""안돼") - 문자열 1개만 기입 가능

# age = int(input("나이를 입력 하세요 : "))

# addr = input("주소를 입력 하세요 : ")

# print("이름 :",name,"\n이 :",age,"\n주소 :",addr)