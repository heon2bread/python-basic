# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한 마리가 하루에
# 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 며칠 만에
# 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇 마리 인가? (쌀 한 통 = 1kg)
# (쌀을 먹은 후 2배 증가하는 조건)

# i=20
# while i>1:
#     i+=20
#     if i%40==0:
#         j=1
#         while j >0:
#             j*=10
#             print(i*j)
#             if i==5000:
#                 break

#변수먼저 정하기
# day=0
# rice=100*1000
# mouse=2
# while rice > 0:
#     day+=1
#     rice-=(mouse*20)
#     if day%10==0:
#         mouse*=2
# print("쌀을 다 먹은날 %d일이고 쥐는 %d마리 입니다."% (day,mouse))

# money=0
# choice=0
# while choice!=1:
#     num=int(input('요금을 투입 하세요\n>'))
#     money=money+num
#     print('현재 금액 : %d원'%money)
#     if money<200:
#         print('========커피 자판기=========')
#         print('1. 반환\t2. 종료')
#         choice=int(input('메뉴를 선택하시거나 돈을 투입해주세요.\n> '))
#         if choice==1:
#             print('%d원 받아가세요.'%money)
#             break
#         elif choice==2:
#             print('종료합니다.')
#             break
#     if money>=250:
#         print('========커피 자판기=========')
#         print('1. 커피<200>\t2. 코코아<250>\t3. 반환\t4. 종료')
#         choice=int(input('메뉴를 선택하시거나 돈을 투입해주세요.\n> '))
#         if choice==1:
#             money-=200
#             print('커피 완료, 거스름돈 %d원 입니다.'% money)
#             break
#         elif choice==2:
#             money-=250
#             print('코코아 완료, 거스름돈 %d원 입니다.'% money)
#             break
#         elif choice==3:
#             print('%d원 받아가세요'% money)
#             continue
#         elif choice==4:
#             print('종료합니다.')
#             break
#     elif money>=200:
#         print('1. 커피<200>\t2. 반환\t3. 종료')
#         choice=int(input('메뉴를 선택하시거나 돈을 투입해주세요.\n> '))
#         if choice==1:
#             money-=200
#             print('커피 완료, 거스름돈 %d원 입니다.'% money)
#             break
#         elif choice==2:
#             print('%d원 받아가세요'% money)
#             continue
#         elif choice==3:
#             print('종료합니다.')
#             break
           

# money=0
# choice=0
# while choice!=4:
#     num=int(input("요금을 투입 하세요 \n>"))
#     money=money+num
#     print("현재 잔액: %d원\n"%money)
#     if money>=250:
#         print("==================커피 자판기==================")
#         print("1.커피(200)\t2.코코아(250)\t3.반환\t4.종료")
#         choice=int(input("메뉴를 선택하세요\n>"))
#         if choice==1:
#             money-=200
#             print("현재 잔액: %d원\n"%money)
#             continue
#         elif choice==2:
#             money-=250
#             print("현재 잔액: %d원\n"%money)
#             continue
#         elif choice==3:
#             money-=money
#             print("현재 잔액: %d원\n"%money)
#             continue
#         elif choice==4:
#             break
#     elif money>=200:
#         print("============커피 자판기============")
#         print("1.커피(200)\t2.반환\t3.종료")
#         choice=int(input("메뉴를 선택하세요\n>"))
#         if choice==1:
#             money-=200
#             print("현재 잔액: %d원\n"%money)
#             continue
#         elif choice==2:
#             money-=money
#             print("현재 잔액: %d원\n"%money)
#             continue
#         elif choice==3:
#             break

# ls=[500, 200, 300, 400]; Sum=0

# print("ls:",ls)
# print("ls[0]:",ls[0])
# print("ls[1]:",ls[1])
# print("ls[2]:",ls[2])
# print("ls[3]:",ls[3])

# - 음수 인덱스 사용
# print("ls:",ls)
# print("ls[0]:",ls[-4])
# print("ls[1]:",ls[-3])
# print("ls[2]:",ls[-2])
# print("ls[3]:",ls[-1])

# ls=[0, 0, 0, 0]; Sum=0

# ls[0]=int(input("첫번째 숫자 입력 : "))
# ls[1]=int(input("두번째 숫자 입력 : "))
# ls[2]=int(input("세번째 숫자 입력 : "))
# ls[3]=int(input("네번째 숫자 입력 : "))

# Sum = ls[0] + ls[1] + ls[2] + ls[3]

# print("ls[0]",ls[0])
# print("ls[1]",ls[1])
# print("ls[2]",ls[2])
# print("ls[3]",ls[3])

# print("리스트의 합 : %d"% Sum)

# ls=[0, 0, 0, 0]; Sum=0

# print("len(ls):",len(ls)) # len 리스트 전체 구성요소의 갯수
# for i in range(len(ls)):
#     ls[i]=int(input(str(i)+"째 숫자 입력 : "))
#     Sum += ls[i]

# for i in range(len(ls)):
#     print("ls[%d]"% i, ls[i])
# print("리스트의 합 : ", Sum)

# ls=[0, 0, 0, 0]
# Sum,i=0,0
# while i<len(ls):
#     ls[i]=int(input(str(i)+"번째 숫자 입력 : "))
#     Sum+=ls[i]
#     i+=1
# else: i=0;
# while i<len(ls):
#     print("ls[%d] : "% i,ls[i])
#     i+=1
# print("리스트의 합 : ", Sum)

# ls = [10,20,30,40]

# print("ls : ",ls)

# print("\nls[1:3] => ls[1]~ls[2] : ",ls[1:3])
# print("ls[0:3] => ls[0]~ls[2] : ",ls[0:3])
# print("ls[2:] => ls[2]~[끝까지] : ",ls[2:])
# print("ls[:2] => ls[0]~[1] : ",ls[:2])