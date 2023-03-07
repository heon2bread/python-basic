# for i in range(0,5):
#     for j in range(0,5):
#         if i==0 and j==0:
#             print('상위포문 %d일때 하위포문 : %d%d%d%d%d'% (i,j,j,j,j,j))
#     if i>0 and j:
#         j+=i
#         print('상위포문 %d일때 하위포문 : %d%d%d%d%d'% (i,j,j,j,j,j))

# for i in range(5):
#     print('상위포문 %d일때 하위포문 :'% i, end='')
#     for j in range(5):
#         print('%3d'% (i*j),end='')
#     print()

# for는 제한적 반복, 규칙적인 패턴을 가진 반복
# while은 무제한적, 불규칙적인 패턴을 가진 반복
# 둘다 반복 종료는 되오나 for은 종료 범위가 보이고 while은 종료 범위가 보이지 않음

# i=0
# while i<5:
#     print(i,'종속 문장')
    # i+=1

# print('다음 문장')

# i=0
# for i in range(5):
#     print(i,'종속 문장')

# print('다음 문장')

# i=1
# odd,even=0,0
# while i<=10:
#     if i %2==0:
#         even+=i
#     else:
#         odd+=i
#     i+=1
# print('1-10 짝수의 합 :',even)
# print('1-10 홀수의 합 :',odd)

# i=0
# while i<5:
#     print(i,'종속 문장')
#     i+=1
# else:
#     print('조건식이 거짓일 경우 :',i)
# print("다음 문장")

# i=1
# while True:
#     print(i,'종속 문장', end="")
#     i+=1

# i=1
# flag=True
# while flag:
#     print(i,"종속 문장",end="")
#     if i==10:
#         flag=False
#     i+=1

# continue, break 만나는순간 위치가 바뀜, 하위로 코드가 올 수 없음

# i=0
# while True:
#     if i ==3:
#         break
#         print('3출력')
#     print(i,'출력')
#     i+=1

# print("다음 문장")

# i=0
# while i<5:
#     i+=1
#     if i==3:
#         print("3 출력")
#         continue
#         # print("3출력")
#     print(i,'출력')
# print('다음 문장')

# num,result,i=0,0,1
# # flag=True
# while True:
#     num=int(input("1~10사이의 숫자 입력 : "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     # else:
#     #     flag=False
#     # print("next...")
#     break
# # print("next...")
# else:
#     print("next...")
# while i<=num:
#     result+=i; i+=1
# else:
#     print('1~',num,"까지의 합 : ", result)

# num,result,i=0,0,10
# while True:
#     num=int(input('10~20사이의 숫자 입력 : '))
#     if num<10 or num>20:
#         print('잘못 입력 다시')
#         continue
#     break
# print('next...')
# while i<=num:
#     result+=i; i+=1
# else:
#     print('10~',num,'까지의 합 : ', result)

# for i in range(0, 3, 1):
#     for k in range(0, 5, 1):
#         if k ==3:
#             break
#         print("(i:%d\tk:%d)"%(i,k))

# i=0
# while i < 3:
#     k=0
#     while k<5:
#         if k ==3:
#             break
#         print('(i:%d\tk:%d)'%(i,k))
#         k+=1
#     i+=1

# for i in range(5):
#     print('상위포문이 %d일때 하위포문 :'%i, end="")
#     for j in range(5):
#         print('%3d'%(i*j),end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print('%d'%(i*j), end='\t')
#     print()