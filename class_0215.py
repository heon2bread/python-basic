# | 버티컬라인, & 엔퍼센트, ^ 캐럿마크, ~ 웨이브대쉬, >> << 쉬프트
# 5(101), 3 (011)
# | or 연산, 2진수로 계산 후 10진수로 변환 = 7
# & and 연산, 2진수로 계산 후 10진수로 변환 = 1
# ^ xor연산, 베타적논리합 올림수 무시 = 6
# ~ not연산, ~는 비트 부정이라고 양수를 음수로 전화하면서 숫자가 1이 커진다. 음수를 비트부정하면 양수로 전환하면서 숫자가 1이 작아진다.
# ~ a -> -a+1
# ~ -a -> a-1
# 0은 양수, 1은 음수
# n의 보수, n-1 보수 (n진수)
# 8 - 2    8 - 1
# 4 - 6    4 - 5
# 8비트에서 가장 큰 수 127, 제일 작은 수 -127
# 5<<2 20, 20>>6 0

# num1 = 3
# num2 = 5
# result = num1 | num2 (or연산)
# print(result)
# num1 = 3
# num2 = 5
# result = num1 & num2 (and연산)
# print(result)
# num1 = 3
# num2 = 5
# result = num1 ^ num2 (xor연산)
# print(result)

# shift연산
# print(5<<2)
# print(20>>2)
# print(20>>6)

# 제어문
# 보통 컴퓨터가 처리하는 순서는 사람이 책을 읽는 방향과 동일하다. 좌에서 우로, 위에서 아래로 진행이 된다.
# 그런데 이러한 순서(방향)을 제어한다 해서 제어문이라는 표현을 쓴다.
# 제어문은 조건 제어문과, 반복 제어문으로 나뉜다.

# 조건 제어문 (분기문)
# if라는 키워드를 사용한다.

# num1=10
# num2=5

# if num1 > num2:                   #종속문장 1개인 경우 : 바로뒤에 붙여도 가능
#     print("num1이 num2보다 크다")

# num1 = int(input("수 입력 : "))

# if num1 % 2 == 0 :
#     print("num1 : ", num1, "짝수다")
# print("나는 다음 문장")

# num1 = int(input("수 입력 : "))
# if num1 % 2 == 0:
#     print("num1 : ", num1, "는 짝수다")
#     print("num1 : ", num1, "는 2의 배수이다")
# print("나는 다음 문장")

# print("1.Easy game")
# print("2.Hard game")
# print("3.Exit")
# num1 = int(input("선택 : "))
# if num1 == 1:
#     print("Easy game start")
# if num1 == 2:
#     print("Hard game start")
# if num1 == 3:
#     print("Game exit")

# day=int(input('날짜 입력 : '))
# if day %7 == 1:
#     print('월요일')
# if day %7 == 2:
#     print('화요일')
# if day %7 == 3:
#     print('수요일')
# if day %7 == 4:
#     print('목요일')
# if day %7 == 5:
#     print('금요일')
# if day %7 == 6:
#     print('토요일')
# if day %7 == 0:
#     print('일요일')

#1
# num1=int(input('숫자 입력 : '))
# if num1 % 3 == 0:
#     print('%d은 3의 배수이다.' % num1)

#2
# num=int(input('숫자 입력 : '))
# if 0<=num:
#     print(num)
# if 0>num:
#     print('절댓값이 아닙니다.')

#3
# num2=int(input('숫자 입력 : '))
# if num2 % 2== 0:
#     print('짝수')
# if num2 % 2==1:
#     print('홀수')

#4
# first=int(input('첫번째 숫자 입력 : '))
# second=int(input('두번째 숫자 입력 : '))
# if first > second:
#     print('%d(이)가 더 크다.' % first)
# if first < second:
#     print('%d(이)가 더 크다.' % second)

#5
# first=int(input('첫번째 숫자 입력 : '))
# second=int(input('두번째 숫자 입력 : '))
# third=int(input('세번째 숫자 입력 : '))
# if first > second and first > third :
#     print('%d(이)가 제일 크다.' % first)
# if second > first and second > third :
#     print('%d(이)가 제일 크다.' % second)
# if third > first and third > second :
#     print('%d(이)가 제일 크다.' % third)

#6
# first=int(input('첫번째 숫자 입력 : '))
# second=int(input('두번째 숫자 입력 : '))
# if first > second and first%2==0:
#     print('%d는 %d보다 크며 짝수이다.' % (first, second))
# if second > first and second%2==0:
#     print('%d는 %d보다 크며 짝수이다.' % (second, first))

#7
# first=int(input('첫번째 숫자 입력 : '))
# second=int(input('두번째 숫자 입력 : '))
# sum=first+second
# if sum % 2 ==0:
#     print('%d, %d의 합은 %d이며, 짝수이고' % (first,second,sum))
# if sum % 3 ==0:
#     print('3의 배수입니다.')

# first=int(input('첫번째 숫자 입력 : '))
# second=int(input('두번째 숫자 입력 : '))
# sum=first+second
# if sum % 2 == 0:
#     print('%d,%d의 합 %d은 짝수이며'% (first,second,sum))
# if sum % 3 == 0:
#     print('3의 배수입니다.')