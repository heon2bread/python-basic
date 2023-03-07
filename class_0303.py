# Str = 'python'

# print('Str\t\t:', Str)

# print('Str.center(10)\t:',Str.center(10))
# print('Str.center(10,"-"):',Str.center(10,'-')) # 한 글자 문자만 대체 가능 [한글(2byte)도 가능]

# print('Str.ljust(10)\t:',Str.ljust(10),Str.ljust(10))

# print('Str.rjust(10)\t:',Str.rjust(10),Str.rjust(10))

# print('Str.zfill(10)\t:',Str.zfill(10)) # 무조건 남은 자리는 0 으로 지정되어 있는 함수여서 다른 문자 지정해서 채울 수 없음

# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# replaceAB = accountBook.split(',') # ,기준으로 리스트로 저장
# k=0
# for i in replaceAB:
#     replaceAB[k]=i.lstrip() # 각 문자열의 왼쪽 공백 삭제 후 저장 (_coffee,_food,_dress)
#     k+=1
# kk='$'
# print('item'.ljust(10),end='')
# print('date'.ljust(10),end='')
# print('$(price)'.ljust(10))

# for i in range(len(replaceAB)):
#     z=replaceAB[i].split() # 공백을 기준으로 리스트로 저장
#     for k in range(len(z)):
#         if k==0:
#             print(z[k].ljust(10),end="") # 10칸 확보 후 왼쪽 출력
#         elif k==1:
#             print(z[k].ljust(10),end="") # 10칸 확보 후 왼쪽 출력
#         elif k==2:
#             print("{:,}".format(int(z[k])).join(kk).ljust(10))

# Str = 'python te12st 1234'

# print("Str.isdigit():",Str.isdigit()) # 숫자로만 구성
# print("Str[9:11].isdigit():",Str[9:11].isdigit()) # 숫자로만 구성

# print("Str.isalpha():",Str.isalpha()) # 글자로 구성
# print("Str[:6].isalpha():",Str[:6].isalpha()) # 글자로 구성

# print("Str.isalnum():",Str.isalnum()) # 글자 + 숫자
# print("Str[7:13].isalnum():",Str[7:13].isalnum()) # 글자 + 숫자 , 공백만 없으면 True

# print("Str.islower():",Str.islower()) # 소문자
# print("Str.isupper():",Str.isupper()) # 대문자
# print("Str.isspace():",Str.isspace()) # 공백

# info = """
# jo 9abc08-3022023
# cho 900402-1011232
# test 1234567-1234567 
# lee 980908-3a2b0c3
# kim 900514-2022023
# """
# lo=0
# while True:
#     lo=info.find('-',lo)
#     if lo != -1:
#         if info[lo+1:lo+8].isdigit() and info[lo-6:lo].isdigit and not(info[lo-7:lo].isdigit()):
#             info=info.replace(info[lo+1:lo+8],'*******')
#         lo+=1
#     else:
#         break
# print(info)

# 함수
# 함수 = function = 기능
# 함수란 어떠한 기능, 동작의 소규모의 프로그램을 정의해놓은 키워드

# 표준 함수와 사용자 정의 함수로 나뉘며
# 표준 함수는 내장 함수와 외부 함수로 나뉜다.

# 함수를 사용하는 이유(목적)
# 1) 코드의 간소화
# 2) 코드의 부품화
# 3) 코드의 수정 편집이 용이
# 4) 전체적인 프로그램의 흐름을 한눈에 알아보기 쉽다.
# 5) 필요한 경우 다른 프로그램에서도 사용 할 수가 있어 생산성을 높을 수 있다. (모듈화)

# result,temp=0,0
# result = int(input("수 입력 : "))
# while True:
#     temp = result%10
#     result = result//10
#     print(temp,end="")
#     if not result: break;
# print("\n프로그램 종료")

# def reverseCode():
#     result,temp=0,0
#     result = int(input("수 입력 : "))
#     while True:
#         temp = int(result%10)
#         result = int(result/10)
#         print(temp,end="")
#         if not result:break;
# print("프로그램 시작")
# reverseCode() # 함수 호출
# print("\n프로그램 종료")

# def calc():
#     result=0
#     su1,op,su2=int(input("숫자:")),input("부호:"),int(input("숫자:"))
#     result = su1+su2
#     print(su1,'+',su2,'=',result)
# calc()

# def calc():
#     result=0
#     su1,op,su2=int(input("숫자:")),input("부호:"),int(input("숫자:"))
#     if op=='+':
#         result = su1+su2
#     elif op=='-':
#         result = su1-su2
#     elif op=='*':
#         result = su1*su2
#     elif op=='/':
#         result = su1/su2
#     print("%d %c %d = %.2f"% (su1,op,su2,result))
# calc()

# def cal(su1,op,su2): # 함수 호출시 전달되는 값을 받는 변수를 매개 변수라고 부름
#     result=0

#     result=su1+su2
#     print(su1,'+',su2,'=',result)

# su1,op,su2= int(input("숫자:")),input("부호:"),int(input("숫자:"))
# cal(su1,op,su2)

# 함수의 호출 유형
# 1) 함수명()
# 2) 함수명(인수1,인수2......)
# 3) 변수명 = 함수명()
# 4) 변수명 = 함수명(인수1,인수2......)

# def cal(su1,op,su2):
#     result=0
#     result=su1+su2
#     print('cal 실행')
#     return result # return은 함수의 종료를 하며, 필요시 함수 호출한 곳으로 값을 반환해줄 수 있습니다.

# su1,op,su2=int(input('숫자:')),input('부호:'),int(input('숫자:'))
# result=cal(su1,op,su2)
# print(su1,'+',su2,'=',result)
# print("다음 문장 실행")

# def showAvrg(a,b,c):
#     print("{}와 {}의 평균".format(a,b))
#     print("값은 {}입니다".format(round(c,1)))
# def avrg(j,k):
#     total=j+k;
#     f=total/2
#     return f;
# i=2; j=3;
# f=avrg(i,j)
# showAvrg(i,j,f)
# print("다음 문장 실행")

# def aa(a):
#     if a ==1:
#         print('1입력')
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print("프로그램 종료")

# def aa(a):
#     if a == 1:
#         return
#         print('1입력') # return은 함수를 종료하므로 하위에 코드와 상관없이 종료함, break와 continue와 마찬가지로 하위의 코드는 실행 할 수 없다.
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print("프로그램 종료")

# def move():
#     print('이동') # 종속문 미정일때 pass로 대체하여 비워놓기 가능
# def attack():
#     print('공격')
# def defense():
#     print('방어')
# move()
# attack()
# defense()

# def func1():
#     a=100
#     print("func1의 a : %d"% a)
# def func2():
#     a=200
#     print("func2의 a : %d"% a)
# func1()
# func2()

# def func1():
#     print("func1의 a : %d"% a)

# def func2():
#     print("func2의 a : %d"% a)

# a = 200 # 전역 변수

# func1()
# func2()

# def func1():
#     a = 123
#     print("func1의 a : %d"% a)

# def func2():
#     print("func2의 a : %d"% a)
# a=200 # 전역 변수
# func1()
# func2()