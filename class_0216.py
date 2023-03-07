# num = int(input("수 입력 : "))
# if num==1:
#     print("1 입력")
# else:
#     print("1이 아닌 값 입력")

# arr = [1,2,3,4,5]
# na = int(input("찾을 숫자 입력 : "))
# if na in arr :
#     print("arr : ", arr,"찾는 숫자가 존재 합니다 : ", na)
# else:
#     print("arr : ", arr,"안에는 찾고자 하는 숫자가 없습니다 : ", na)
# print("결과 : ", na in arr)

# A in B 에서 in은 멤버 연산자라고 부릅니다.
# 뜻은 B안에 A가 존재하면 참이고 존재하지 않으면 거짓입니다.
# A not in B 는 B안에 A가 존재하지 않으면 참이고 존재하면 거짓입니다.
# 즉 in과 not in은 결과값을 True나 False로 반환합니다.

# st = "Hello Python Fun"
# na = input("찾고자 하는 문자열 입력 : ")
# if na in st:
#     print("st : ", st,"찾는 문자열 : ", na,"존재한다.")
# else:
#     print("st안에는", na,"존재하지 않습니다.")

# old_id = input("저장할 ID 입력 : ")
# print("인증 프로그램 입니다")
# print("ID와 PW를 입력하세요")
# new_id = input("ID를 입력 : ")
# if old_id == new_id:
#     print("인증 통과 했습니다")
# else:
#     print("인증 실패")

# num = int(input("수 입력 : "))
# if num %3==0:
#     if num %2==0:
#         print("num은 3의 배수이면서 짝수 입니다.")
# print("다음 문장 실행")

# if num %3==0 and num %2==0:
#     print("num은 3의 배수이면서 짝수 입니다.")
# print("다음 문장 실행")

# num = int(input("수 입력 : "))
# if num >= 0:
#     if num %2==0:
#         print("%d은 양의 짝수 입니다."%num)
#     else:
#         print("%d은 양의 홀수 입니다"%num)
# else:
#     print("%d은 음수 입니다."%num)
# print("다음 문장 실행")

# naver
# oldid=input('ID를 입력하세요 : ')
# oldpw=input('PW를 입력하세요 : ')
# print('===========인증프로그램 시작===========')
# newid=input("ID를 입력하세요 : ")
# newpw=input('PW를 입력해주세요 : ')
# if oldid==newid:
#     if oldpw==newpw:
#         print('인증 통과')
#     else:
#         print('비밀번호가 틀렸습니다.')
# else:
#     print('존재하지 않는 아이디입니다.')

# google
# oldid=input('ID를 입력하세요 : ')
# oldpw=input('PW를 입력하세요 : ')
# print('===========인증프로그램 시작===========')
# newid=input("ID를 입력하세요 : ")
# if oldid==newid:
#     newpw=input('존재하는 ID입니다. PW를 입력해주세요 : ')
#     if oldpw==newpw:
#         print('인증 통과')
#     else:
#         print('비밀번호가 틀렸습니다.')
# else: 
#     print('존재하지 않는 아이디입니다.')

# num = int(input("수 입력 : "))
# if num > 100:
#     print("100보다 큰 수 입력")
# elif num > 50:
#     print("50보다 큰 수 입력")
# elif num > 0:
#     print("0보다 큰 수 입력")
# else:
#     print("그 외의 값 입력")

# 1
# name=input('이름 입력 : ')
# number=input('학번 입력 : ')
# ko=int(input('국어 점수 입력 : '))
# en=int(input('영어 점수 입력 : '))
# ma=int(input('수학 점수 입력 : '))
# sum=ko+en+ma
# avg=sum/3
# print('학번 %d의 %s의 평균은 %d이며'% (number, name, avg))
# if avg >=90:
#     print('A등급 입니다.')
# elif avg >=80:
#     print('B등급 입니다.')
# elif avg >=70:
#     print('B등급 입니다.')
# elif avg >=60:
#     print('B등급 입니다.')
# elif avg < 60:
#     print('F등급 입니다.')
# +
# if avg >=90 : level = 'A'
# elif avg >=80 : level = 'B'
# elif avg >=70 : level = 'C'
# elif avg >=60 : level = 'D'
# else : level = 'F'
# print('=============학생 정보============')
# print('이름\t학번\t국어\t영어\t수학\t총점\t평균\t학점')
# print('%s\t%s\t%d\t%d\t%d\t%d\t%.2f\t%c'% (name,number,ko,en,ma,sum,avg,level))

# 2
# buy=int(input('구매 할 커피의 수 : '))
# cof1=2000
# sale=1500
# salebuy=(buy-10)*sale
# price=cof1*buy
# if buy <= 10:
#     print('%d원 입니다.'% price)
# elif buy > 10:
#     print('%d원 입니다.'% (20000+salebuy))
# +
# coff=int(input('주문 커피 수량 : '))
# if coff > 10 :
#     money=2000 * 10 + (coff-10)*1500
# else:
#     money=2000*coff
# print('주문한 커피 금액 : %d원'% money)

# 3
# num=int(input('정수 입력 : '))
# if 0<num %3==0:
#     if 0<num %4==0:
#         print('%d은(는) 3의 배수이면서 4의 배수입니다.'% num)
# elif 0<num %4==0:
#     print('%d은(는) 4의 배수입니다.' % num)
# elif 0<num %3==0:
#     print('%d은(는) 3의 배수입니다.'% num)
# elif num==0:
#     print('0은 3의 배수도 4의 배수도 아닙니다.')
# else:
#     print('%d은(는) 3의 배수도, 4의 배수도 아닙니다.' % num)
# +
# num1 = int(input('정수 입력 : '))
# if num1 == 0 :
#     print('0은 3의 배수도 4의 배수도 아닙니다.')
# elif num1 %3 == 0 and num1 %4==0:
#     print('3의 배수이면서, 4의 배수입니다.')
# elif num1 %3 == 0:
#     print('3의 배수입니다.')
# elif num1 %4 == 0:
#     print('4의 배수입니다.')
# else:
#     print('3의 배수도 4의 배수도 아닙니다.')

# 4
# time=int(input('시간(분)을 입력하세요 : '))
# time30=30000
# over=time-30 or time-29 or time-28 or time-27 or time-26 or time-25 or time-24 or time-23 or time-22 or time-21
# time10=5000*(over//10)
# if time <= 30:
#     print('30000원 입니다.')
# elif time < 40:
#     print('35,000원 입니다.')
# elif time > 39:
#     print(5000+time30+time10)
# +
# money = 30000
# time=int(input('비행기 탑승시간 입력(분) : '))
# time-=30
# if time > 0 :
    # money+=((time-1)//10*5000+5000) # 한번에 풀 수 있는 계산식☆
    # if time %10 == 0 : # 탑승시간이 10분 단위로 떨어질때 40분, 50분, 60분~
    #     money+=(time//10*5000)
    # else : # 탑승시간이 분단위로 떨어질때 41분, 53분, 72분 ~
    #     money+=(time//10*5000+5000)
# print('비행기 탑승 요금 : %d원' % money)