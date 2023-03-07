# 문자열
# Str = 'Have a nice day'

# print("Str[0] : ", Str[0])
# print("Str[1] : ", Str[1])
# print("Str[2] : ", Str[2])
# print("Str[3] : ", Str[3])
# print()
# print("문자열의 총 길이 : ", len(Str))
# print("Str : ", Str)

# for i in range(len(Str)):
#     print(Str[i],end="")
# print('\n')
# for i in Str:
#     print(i, end='')
# print()

# Str = 'Have a nice day'

# arr = Str[7:11]
# print("Str : ", Str)
# print("arr : ", arr)

# Str="즐거운 파이썬"
# print("Str\t:", Str)
# print("Str[0]\t:", Str[0])
# print("Str[1;3]:", Str[1:3])
# print("Str[3:]:", Str[3:])
# print("Str[:3]:", Str[:3])

# Str='Have a'
# print('변경 전 Str : ', Str)
# 
# Str+=' nice day'
# 
# print("변경 후 Str : ", Str)
# print("Str * 3 : ", Str*3)

# Str='Python is Easy. 그리고 programming 할만하다^^'
# print("Str : ", Str)
# print()
# print("Str.upper() : ", Str.upper()) # 소문자를 대문자로 변경
# print()
# print("Str.lower() : ", Str.lower()) # 대문자를 소문자로 변경
# print()
# print("Str.swapcase() : ", Str.swapcase) # 대소문자 상호 변경
# print()
# print("Str.title() : ", Str.title()) # 각 단어의 첫번째 문자 대문자로 변경)

# st = 'NevEr -eVer 110gIVeup' # 한글, 특수문자, 숫자는 함께 단어로 표현하지 않으며 연속성도 한 단어로 인식

# st=st.title()

# print(st)

# st='Have a nice day'
# print("st : ",st)
# print()
# # print("st안에 'a'문자 개수 : ", st.count('a'))
# # print("st안에 'day'문자열 개수 : ", st.count('day'))
# # print("st안에 'dak'문자열 개수 : ", st.count('dak'))
# print(st.count('')) # 맨 끝에 \널 문자가 있어서 1개 더 세어야됨

# st='Have a nice day'
# print("st : ", st)

# print("find : 'day'위치 : ", st.find('day'))
# print("index : 'day'위치 : ", st.index('day'))
# print("find : 'kkk'위치 : ", st.find('kkk'))
# print("index : 'kkk'위치 : ", st.index('kkk'))

# st='Have a nice day'
# print("st : ",st)

# print("find: 'day'위치 : ", st.find('a'))
# print("find: 'day'위치 : ", st.find('a',2)) # (찾기 시작 할 위치 지정)
# print("find: 'day'위치 : ", st.find('a',6))
# print("find: 'day'위치 : ", st.find('a',14))

# st='Have a nice day Have a nice day Have a nice day'
# lo=0 # 위치 지정을 해줌과 동시에 찾은 위치를 저장할 변수 (처음부터 찾기 위해서 0으로 초기화)
# ls=[]
# while True:
#     lo=st.find('a',lo)
#     if lo != -1: # -1과 같지 않다는 것은 존재하는 a의 위치값을 반환받은거임
#         ls.append(lo) # 그래서 추가해줘야함
#         lo+=1 # 1을 더해줘서 찾은 위치 다음 인덱스부터 다시 검색
#     else: # else라면 -1과 같다는 것이고 더 이상 존재 하지 않으므로 반복을 끝냄
#         break
# print('a의 개수 : %d'%st.count('a'))
# print(ls)

# st='    파 이 썬    '

# print('st\t\t:{}{}{}'.format('*',st,'*'))
# print()
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))

# st='파이썬파'

# print('st\t\t:',st) 
# print()
# print('Str.strip("파")\t:',st.strip('파')) # 연속적인 2글자 이상도 양쪽 삭제 가능
# print('='*20)

# st='파이썬'
# print('st\t\t:',st)
# print()
# print('Str.strip("파")\t:',st.strip("파"))  

# st='---파---이---썬---'
# print('st\t\t:',st)
# print('st.strip("-")\t:',st.strip('-'))

# print('st.rstrip("-")\t:',st.rstrip('-'))

# print('st.lstrip("-")\t:',st.lstrip('-'))

# st='2015/04/02'

# print('st\t\t:',st)
# print('replace()\t:',st.replace('/','.'))
# print('replace([0:4])\t:',st.replace(st[0:4],'2017'))

# st="""
# 오늘 하루도 즐겁게
# 오늘 하루도 행복하게
# 오늘 하루도 최선을
# """

# print(st)

# ''' 3개로 열고닫아 여러행 표현, 끝에 \n이 들어가 있음

# st="""
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# """
# st=st.replace('-',':')
# lo=0
# while True :
#     lo=st.find(':',lo)
#     if lo != -1:
#         st=st.replace(st[lo+1:lo+5],'1999')
#         lo+=1
#     else:
#         break
# print(st)

# st="""
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# """
# st=st.replace('-',':')
# lo=0
# while True :
#     lo=st.find('년',lo)
#     if lo != -1:
#         st=st.replace(st[lo-4:lo],'1999')
#         lo+=1
#     else:
#         break
# print(st)

# st='Never ever give up'

# print('st\t\t:',st)
# print('st.split()\t:',st.split())

# st='하나:둘:셋'

# print('st\t\t:',st)

# print('st.split(:)\t:',st.split(':'))

# st='일,이,삼'
# print('st.split(,)\t:',st.split(','))

# st='Never ever give up'
# print('st : ',st)
# print('st.splitlines():',st.splitlines())
# st='''
# Never ever give up
# Never ever give up
# '''
# print('st.splitlines():', st.splitlines())
# st="하나\n둘셋"
# print('st.splitlines():',st.splitlines())

# Str='123'
# print('"%".join(123)\t:','%'.join(Str))
# print('123.join("%a")\t:',Str.join('%a'))

# li=['','123','456']
# print('"공백".join([123.456])\t:',"".join(li))
# li=['','안녕하세요','만나서 반갑습니다','행복한 하루 되세요^^']
# print('"엔터".join(li)\t:',"\n\n".join(li))

# a.join(b) 는 b의 구성요소 사이마다 a를 끼워넣기 하는 함수입니다.
# 그래서 b는 주로 시퀀스형 자료형만 사용될겁니다. (문자열, 리스트, 튜플)

# Str=123
# print('"%".join(123)\t:,'%'.join(Str))
