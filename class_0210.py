# 변수란?
# 메모리에 저장되는 데이터들의 공간에 이름을 붙여 사용
# -> 메모리의 저장은 랜덤이므로 재가공 하기 위해 메모리 공간에 이름을 부여해 재가공을 하기 위함.

# 변수의 이름은 알파벳, 숫자, 언더바(_)로 구성 + 특수문자, 한글
# 대소문자 구분
# 변수의 이름은 숫자로 시작할 수 없음
# 키워드(예약어)는 변수 이름으로 사용 불가능
# 공백이나 특수 기호는 포함될 수 없음
# 안지키면 에러 발생

# 변수명 작명요령
# 1) 변수는 그 프로그램 내에서 어떤 기능을 하는지 또는 어떤 내용을 저장하는지 쉽게 연상할 수 있도록 지어주는 것이 바람직하다.
# 예) 이름 -> name , 나이 -> age , 년도 -> year
# 2) 한글 변수는 사용 가능하다. 하지만 프로그램 작성시 사용하지 않는 것이 바람직하다.

# num = 100
# print("정수형 변수 사용 : %d" % num)
# print("정수형 변수 사용 :", num)

# =는 대입연산자입니다. 유일하게 진행방향이 우에서 좌로 진행됩니다.
# 변수 = 상수
# 변수 = 변수(값을 갖고 있는 변수, 정의되어 있는 변수)
# 변수 = 연산식
# 변수 = 함수
# 좌측은 무조건 변수만 올 수 있음

# sum - 범위의 누적 합의 함수
# id - 주소값
# num1 = 5
# print("id num1 : ",id(num1))
# num2 = 10
# num1 = num1+num2
# print("id num1 : ",id(num1))
# print(id (15))

# num1 = 10
# num2 = 20
# print("num1(",num1,")+num2(",num2,")=",num1+num2)
# print("num1(%d) + num2(%d) = %d"%(num1,num2,num1+num2))

# num1=7
# num2=5
# sum_=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# print("num1(%d) + num2(%d) = %d"% (num1,num2,sum_))
# print("num1(%d) - num2(%d) = %d"% (num1,num2,sub))
# print("num1(%d) * num2(%d) = %d"% (num1,num2,mul))
# print("num1(%d) / num2(%d) = %.1f"% (num1,num2,div))

# age=27
# # 파이썬=100
# py=60
# clang=60
# java=70
# sum_=py+clang+java
# avg=(sum_)/3
# # print("파이썬 = %d점"% 파이썬)
# # print("나는 %d살 입니다." % age)
# print("총점 : %d,평균값 : %.2f "% (sum_,avg))

# sub=11
# time=37
# one=time/sub
# print("지나온 역의 수와 걸린시간 : %d개, %d분 \n한 역 지나는데 걸리는 시간 : %.2f분"% (sub,time,one))
# print("\n한 역 지나는데 걸리는 시간 : %.2f분"% (one))

# flt = 123.567
# print("round(flt):",round(flt))
# print("round(flt,1)",round(flt,1))
# print("round(flt,2)",round(flt,2))
# round - 반올림 함수, 정수 부분도 반올림 가능 (가공 가능)