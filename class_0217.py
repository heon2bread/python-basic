# 반복문 (=순환문)
# 특정 연속적인 구간을 조건에 의하여 반복 순환한다 하여 반복 순환문이라 합니다.
# 반복문은 for 와 while로 나뉩니다.
# 둘의 용도 구분은 while문에서 알려드리겠습니다.

# for i in range(1, 11, 1) : # 이 행을 반복 구문이라고 표현하며 반복의 횟수를
#             # (i=1, 1<11 . i+=1) - c언어 표현
#     print(i)

# print('다음 문장')

# for i in range(1, 11, 1) :
#     if i %2==0 :
#         print("i=",i,": 값 확인")

# print("다음 문장")

# for i in range(0, 11, 2):
#     print("i = ", i , ": 값 확인")

# for i in range(10, -1, -1) :
#     print(i, ": 10 ~ 0 까지 출력")

# sum=0
# for i in range(1, 11, 1):
#     sum+=i
# print(sum)

# for i in range(1, 11, 1):
#     print(i, end="문자") # end : 모두 자동\n대신 다른 것 사용하려고 할 때, 문자열 1개만 가능

# for i in range(1,31,1):
#     if i %5==1 :
#         print('\n')
#     print(i, end='\t')
# +
for i in range(1,31,1):
    print(i,end='\t')
    if i%5==0:
        print()

# i, Sum = 0, 0
# start, en, grow = 0, 0, 0

# start = int(input('시작값 입력 : '))
# en = int(input('끝값 입력 : '))
# grow = int(input('증가값 입력 : '))

# for i in range(start, en+1, grow):
#     Sum = Sum + i

# print("%d에서 %d까지 %d씩 증가한 값의 합 : %d" % (start, en, grow, Sum))

# for i in range(0,10): # 증감값 1로 기본 세팅
#     print(i)
# for i in range(10): # 시작 0으로 기본 세팅
#     print(i)
# for i in range(10, 2): # 증감값 1로 기본 세팅 되어있어 불가
#     print(i)
# for i in range(0,10,2):
#     print(i)

#1
# start = int(input('시작값 입력 : '))
# end = int(input('끝값 입력 : '))
# grow = int(input('증가값 입력(1) : '))
# print('%d부터 %d까지 7의 배수는'% (start,end))
# for i in range (start, end+1, grow):
#     if i %7==0:
#         print(i,end='\t')
# print('입니다.')

#2
# sum=0
# for i in range(1,101,1):
#     if i%3==0 and i%5==0: # 1%15==0 X
#         sum+=i
# print('결과 :', sum)

#3
# sum=0
# num1 = int(input('첫번째 숫자 입력 : '))
# num2 = int(input('두번째 숫자 입력 : '))
# if num1 > num2:
#     for i in range(num2,num1+1):
#         sum+=i
# elif num2 > num1:
#     for j in range(num1,num2+1):
#         sum+=j
# print('결과 : ',sum)

#4
# for i in range(1,310,1):
#     if i==1 :
#         print(i*10)
#     elif i>1 :
#         i*=2
#         print(i)
# +
# money=10
# save=10
# for i in range(2,31) : # 반복은 2일차부터 시작이고 30일에 끝나야 함
#     money*=2
#     save+=money
#     print('입금액 : %d / 저축금액 : %d'% (money, save))
# print("마지막 입금액 : %d원\n총 저축금액 : %d원 : "% (money,save))