# thisyear=int(input('올해의 년도를 4자리로 입력하세요\n'))
# bornyear=int(input('당신이 태어난 년도를 4자리로 입력하세요\n'))
# age=thisyear-bornyear+1
# print('당신의 나이는 %d세 입니다.'% age)
# print('당신의 나이는 %d세 입니다.'% (thisyear-bornyear+1))

# first=float(input('첫번째 물건의 무게 : '))
# second=float(input('두번째 물건의 무게 : '))
# can=600-first-second
# print('현재 엘레베이터의 허용 무게는 %.2fkg 입니다.'% can)
# print('현재 엘레베이터의 허용 무게는 %.2fkg 입니다.'% (600-first-second))

# tall=float(input('현재 키를 입력하세요 : '))
# kg=int(input('현재 체중을 입력하세요 : '))
# avg=(tall-100)*0.9
# fat=(kg/avg)*100
# print('표준 체중은 %.1fkg이고 비만도는 %.2f%%입니다.'% (avg,fat))

# print('<결과>\n')

# name=input('학생 이름 : ')
# korean=int(input('국어 점수 : '))
# english=int(input('영어 점수 : '))
# math=int(input('수학 점수 : '))
# sum=korean+english+math
# avg=round((sum/3),2)
# print('====================학생 정보====================')
# print('이름\t국어\t영어\t수학\t합계\t평균')
# print(name,'\t',korean,'\t',english,'\t',math,'\t',sum,'\t',avg)
# print('%s\t%d\t%d\t%d\t%d\t%.2f' % (name,korean,english,math,sum,avg))

# num1=9;num2=2

# print(num1,"+",num2,"=",num1+num2)
# print(num1,"-",num2,"=",num1-num2)
# print(num1,"*",num2,"=",num1*num2)
# print(num1,"/",num2,"=",num1/num2)
# print(num1,"//",num2,"=",num1//num2)
# print(num1,"%",num2,"=",num1&num2)
# print(num1,"**",num2,"=",num1**num2)

# su1=3.1; su2=3

# print("su1 >= su2 : ", (su1>=su2))
# print("su1 <= su2 : ", (su1<=su2))
# print("su1 == su2 : ", (su1==su2))
# print("su1 != su2 : ", (su1!=su2))
# 0을 제외한 모든 데이터는 참 / 0은 무조건 거짓

# su1=su2=5
# su1+=1
# print("su1 + 1 =", su1)
# su1-=1
# print("su1 - 1 =", su1)
# su1*=su2
# print("su1 * su2 =", su1)
# su1//su2
# print("su1 // su2 =", su1)
# su1%=su2
# print("su1 % su2 =", su1)

# su1=5
# su2=3
# su1**=su2
# su1-=2
# print("su1 / 4 =", su1/4)
# print("su1 // 4 =", su1//4)
# print("su1 % 4 =", su1%4)

# and 연산에서 좌측이 false나오면 우측은 아무것도 처리 안함
# or 연산은 좌측이 true나오면 우측은 아무것도 처리 안함

# print(0 or 0,":",False or False)
# print(1 or 0,":",True or False)
# print(0 or 1,":",False or True)
# print(1 or 1,":",True or True)

# print("not : ",not(0 or 0),":",not(False or False))
# print("not : ",not(1 or 1),":",not(True or True))

# print(0 and 0,":",False and False)
# print(1 and 0,":",True and False)
# print(0 and 1,":",False and True)
# print(1 and 1,":",True and True)

# print("not : ",not(0 or 0),":",not(False or False))
# print("not : ",not(1 or 1),":",not(True or True))

# a=20
# b=10
# print(False or (a+b)) # 좌측 false 무시
# print(True or (a+b)) # 우측 (a+b) 무시
# print(False and (a+b))
# print(True and (a+b))