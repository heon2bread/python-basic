# List=[22, 1, 33, 4, 19, 2, 44, 7, 33,15, 8]
# print("현재 리스트:",List)

# del(List[2]) # 인덱스 지정 삭제한 후 뒤에 데이터들은 자리가 앞으로 땡겨짐
# print("del[2]후 리스트 : ",List)

# List.sort() # 오름차순 정렬
# print("sort()후 리스트 : ",List)

# List.reverse() # sort 다음 reverse를 하게 되면 내림차순 정렬 가능
# print("reverse()후 리스트 : ",List)

# print("pop()으로 추출한 값 : ",List.pop())
# 맨 마지막 데이터를 삭제해야 할 때 / ()안에 인덱스를 지정해주면 인덱스 값을 추출하여 제거 / 
# remove나 del은 값이나 인덱스가 있어야 삭제 가능
# print("pop()후 리스트 : ",List)

# List.append(40)
# print("append(40)후 리스트 : ",List)

# List=[22, 1, 33, 4, 19, 2, 44, 7, 33,15, 8]
# print("현재 리스트:",List)

# print("10값의 위치 :",List.index(33)) # 중복 데이터일 경우 앞의 자리를 표시

# List.insert(2,200)
# print("insert(2,200) 후 리스트 :",List)

# List.remove(1)# 중복 데이터일 경우 앞의 자리를 삭제
# print("remove(1) 후 리스트 :",List)

# List.extend([555, 666, 555])
# print("extend([555, 666, 555]) 후의 리스트 :",List)

# print("555의 개수 :",List.count(555))

# ls=[10, 5, 20, 7, 9, 31 ,12, 11, 19, 32]

# jjak=[]
# hol=[]
# ret=[]
# for i in range(len(ls)):
#     if i%2==0:
#         hol.append(ls[i])
#     else:
#         jjak.append(ls[i])
# for j in range(len(hol)):
#     ret.append(jjak[j]-hol[j])
# print(ret)

# ls=[10, 5, 20, 7, 9, 31 ,12, 11, 19, 32]
# jjak_sum=0; hol_sum=0

# for i in range(len(ls)):
#     if i%2==0:
#         jjak_sum+=ls[i]
#     else:
#         hol_sum+=ls[i]
# print(jjak_sum-hol_sum)

# ls=[10, 5, 20, 7, 9, 31 ,12, 11, 19, 32]
# invertls=[]
# for i in range(1,len(ls)+1):
#     invertls.append(ls[-i])
# print(invertls)
# +
# temp=ls[:]
# invertls=[]
# for i in range(len(ls)):
#     invertls.append(temp.pop())
# print(invertls)
# +
# cnt=10
# invertls=[]
# for i in range(len(ls)):
#     cnt-=1
#     invertls.append(ls[cnt])
# print(invertls)

# ls=[10, 5, 20, 7, 9, 31 ,12, 11, 19, 32]
# sortls=ls[:] # 깊은복사, 원본 훼손하지 않기 위해
# for i in range (len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if sortls[i] > sortls[j]:
#             sortls[i],sortls[j]=sortls[j],sortls[i]
# print(sortls)

# ls=[10, 5, 20, 7, 9, 31 ,12, 11, 19, 32]
# reversels=ls[:]
# for i in range (len(ls)-1):
#     for j in range(i+1,len(ls)):
#         if reversels[i] < reversels[j]:
#             reversels[i],reversels[j]=reversels[j],reversels[i]
# print(reversels)

# aa=[[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]]

# print('[0][0]',aa[0][0])
# print('[0][1]',aa[0][1])
# print('[0][2]',aa[0][2])
# print('[0][3]',aa[0][3])
# print('[1][0]',aa[1][0])
# print('[1][1]',aa[1][1])

# for i in range(len(aa)):
#     for j in range(len(aa[i])):
#         print(aa[i][j],end='\t')
#     print()
# print()

# for i in aa:
#     for j in i:
#         print(j, end='\t')
#     print()

# aa=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# a=aa[0]
# a[1]=20000

# print('[0]',aa[0])
# print(a)
# print(aa)

# import copy
# aa=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# #a=aa[0][:] # 슬라이싱으로 하게 될 경우 얕은 복사가 되어버림
# a=copy.deepcopy(aa[0])
# a[1]=20000

# print('[0]',aa[0])
# print(a)
# print(aa)

# ls=[]
# ls2=[]
# value=1
# aa=[]
# i=0
# print('===========================')

# if i == 0:
#     ls.append(i)
# for j in range(0,12):
#     ls2.append(j)
#     print(ls[i]+ls2[j]+value,end='\t')
#     if (i+j+value)%4==0:
#         print(end='\n')
# +
# ls_1=[];ls_2=[];value=1
# for i in range(3):
#     for j in range(4):
#         ls_1.append(value)
#         value+=1
#     ls_2.append(ls_1)
#     ls_1=[]
# for i in ls_2:
#     for j in i:
#         print(j,end='\t')
#     print()

# print(ls_2)