# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("i :",i)
# 차례대로 불러옴

# ls = [1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     print("i :",i)
# for i in ls:
#     print(i,end="")

# ls = [10, "test", 123.123]
# print("list : ", ls)
# print()
# for i in ls:
#     print("i에",i,"대입한 후 print() 실행")
#     print(type(i))

# st = "Hello Python"
# for i in st:
#     print("i :",i)
# for i in st:
#     print(i,end="")
# print()

# st = "It is a fun Python class"
# to_ont=0;a_ont=0;s_ont=0
# for i in st :
#     to_ont+=1
#     if i=='a' :
#         a_ont+=1
#     elif i=='s' :
#         s_ont+=1
# print("총 개수 : %d\na 개수 : %d\ns 개수 : %d"%(to_ont,a_ont,s_ont))

# print("{0}+{1}={2}".format(10,2,10+2))
# print("{2}+{1}={0}".format(10,2,10+2))
# print("{}+{}={}".format(10,2,10+2)) # 비워두면 차례대로 대입

# print("{:,}".format(1000000))

# print("{:<10},왼쪽 정렬,{:0<10}".format('첫번째','두번째'))
# print("{:>10},오른쪽정렬,{:9>10}".format('첫번째','두번째'))
# print("{:^10},가운데정렬,{:5^10}".format('첫번째','두번째'))
# 중앙 정렬시 확보되는 칸수와 채워지는 글자수의 밸런스가 맞아야 딱 중앙 정렬
# 만일 짝 홀수 밸런스가 맞지 않은 경우 맨 우측 한 칸이 없다고 간주하고 중앙 정렬함
# 그래서 오른쪽 한칸이 더 남음
# print('{:.2f}'.format(3.141592))
# print('{:f}'.format(3.141592))
# print('{:d}'.format(3))

# for i in range(0, 3, 1):
#     for k in range(0, 5, 1):
#         print("이중 for 문 (i:%d\tk:%d)"%(i,k))

# for i in range(1,10,1):
#     for k in range(2,10,1):
#         x=k*i
#         print("%dx%d=%d"%(k,i,x),end='\t')
#     print()

# print("\t\t\t구 구 단")
# print('============================================================')
# for k in range (2,10):
#     print("%d단"%k,end='\t')
# print()
# print('============================================================')
# for i in range(1,10):
#     for j in range(2,10):
#         print("%dX%d=%d"%(j,i,j*i),end="\t")
#     print()