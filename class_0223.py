# 얕은 복사 (데이터가 동기화가 되어야하는 것들)
# ls=[10, 20, 30, 40]
# arr=ls # ex) 재고수량과 출고수량 연산
# print("ls : {}ls, id : {}".format(ls,id(ls)))
# print("arr : {}arr, id : {}".format(arr,id(arr)))

# ls=[10, 20, 30, 40]
# arr=ls
# arr[2]=20000
# print("ls : {}ls, id : {}".format(ls,id(ls)))
# print("arr : {}arr, id : {}".format(arr,id(arr)))

# 깊은 복사 (ex. 입고수량과 재고수량 연산(원본은 유지해야 할때))
# ls=[10,20,30,40]
# arr=ls[:] # [:] 처음부터 끝까지 개채를 한 개 더 생성, 

# arr[2]=20000 # 20000으로 변경해도 원본은 그대로 유지, id 주소값 서로 다름

# print("ls : {}, ls id : {}".format(ls,id(ls)))
# print("arr : {}, arr id : {}".format(arr,id(arr)))

# 가급적이면 깊은 복사는 슬라이싱 아닌 함수를 사용 권장

# from copy import deepcopy # (from ~라는 모듈안에 import ~의 함수만을 사용)
# # import copy
# ls=[10, 20, 30, 40]
# # arr=ls[:]
# # arr=copy.deepcopy(ls) # copy라는(출처밝힘) 모듈안에 deepcopy는 외부함수를 사용
# arr=deepcopy(ls)
# arr[2]='deepcopy'

# print("ls : {}, is id : {}".format(ls,id(ls)))
# print("arr : {}, arr id : {}".format(arr,id(arr)))

# 표준 함수

# 내장 함수(ex. print())
# 인터프리터에 포함되어 있어 별도의 문법 없이 함수를 호출만으로 바로 사용 가능하다.

# 외부 함수
# 프로그램 설치시 저장장치에 저장되었다가 import라는 문법으로 문서에 가져와서 사용 할 수 있다.

# ls=[10, 20, 30]
# arr=[40, 50, 60]

# print("ls : ",ls)
# print("arr : ",arr)

# Str=ls+arr # 시퀀스형이여서 데이터 이어붙이기
# print("ls+arr => Str : ", Str)

# string=ls*3
# print("ls*3 => string : ", string)

# ls=[10, 20, 30]
# arr=[40, 50, 60]
# Str=[0,0,0]
# string=[0,0,0]
# for i in range(len(ls)):
#     Str[i] = ls[i] + arr[i]
#     string[i] = ls[i]*3
# print(Str)
# print(string)

# 정렬 알고리즘

# ls=[4,8,2,7,6]

# for i in range(len(ls)-1): # 기준 인덱스 지정
#     for j in range(i+1, len(ls)) : # 비교 대상 인덱스 지정
#         if ls[i] > ls[j]:
#             ls[i],ls[j]=ls[j],ls[i]
# print(ls)

# ls=[82, 85, 76, 79, 96]
# stls=[1,1,1,1,1]

# for i in range(len(ls)):
#     for j in range(len(ls)):
#         if ls[i] < ls[j]:
#             stls[i]+=1
# for k in range(len(stls)):
#     print("점수 : %d / %d등"% (ls[k],stls[k]))

# ls=[10,20,30]
# ls.append(1000)

# for i in range(len(ls)):
#     print("ls[{}]:{}".format(i,ls[i]))
# print("리스트의 총 개수 :",len(ls))
# print("ls :",ls)
# ls=[]
# print("ls초기화 후 : ",ls)

# ls=[]
# for i in range(0,4):
#     ls.append(0)
# Sum=0

# for i in range(0, len(ls)):
#     ls[i]=int(input(str(i+1)+"번째 숫자 : "))
#     Sum +=ls[i]

# for i in range(0,len(ls)):
#     print("입력 받은 값 ls[{}] : {}".format(i,ls[i]))
# print("합계 : %d"% Sum)

# num=int(input("몇개의 공간 만들겠습니까? : "))
# ls=[]
# Sum=0
# for i in range(num):
#     ls.append(int(input(str(i+1)+'번째 숫자 : ')))
#     Sum+=ls[i]

# # for i in range(0, len(ls)):
# #     print("입력 받은 값 ls[{}]:{}".format(i,ls[i]))
# print('합계 : ',Sum)
