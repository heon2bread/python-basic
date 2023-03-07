# student={'학번':1234, '이름':'홍길동', '학과':'it학과'}

# print(student['학번'])
# print(student['이름'])
# print(student['학과'])
# print()
# print(student.items()) # 튜플과 리스트 속성을 함께 가지고 있다.
# print()
# print(student)

# name={'이순신':"거북선","세종대왕":'훈민정음','파이썬':'프로그래밍 언어'}
# for key,value in name.items():
#     print(key,":",value)

# print("삭제 : ",name.clear())
# print("삭제 후 값 :", name)

# num={1:'일',2:'이',3:'삼',4:'사',5:'오'}

# print("변경 전 값 : ", num)
# print()
# print("num.setdefault(9) : ",num.setdefault(9,"구~우"))
# print()
# print("변경전 후 : ",num)
# print()
# print("num.get(9)번째 value : ", num.setdefault(5,"오~우")) # 원본 데이터 변경 불가
# print()
# print("변경 후 : ",num)

# num={1:'일',2:'이',3:'삼',4:'사',5:'오'}
# aaa={6:'육',7:'칠',8:'팔'}

# print("update 전 num : ", num)
# num.update(aaa)

# print("update 후 num : ", num)

# dic={}
# ls=[]

# ls.append(input('등록된 키값 입력 : '))
# ls.append(input('등록된 키값 입력 : '))
# ls.append(input('등록된 키값 입력 : '))

# dic = dic.fromkeys(ls)
# print("dic키 설정 : ",dic)

# dic=dic.fromkeys(ls,0)
# print("dic 키&값 설정 : ", dic)

# print(ls)
# print(dic)

# num={1:'일',2:'이',3:'삼',4:'사'}

# print("pop전 num : ", num)
# print("\npop(3)실행 : ", num.pop(3))
# print("\npop 실행 후 num : ", num)

# num={1:'일',2:'이',3:'삼',4:'사',5:'오'}

# print("popitem()전 num : %s\n"% num)

# print("popitem 실행 결과 => ",end="")
# print(num.popitem()) # 추출로 마지막 데이터 삭제
# print("popitem()후 num : %s\n"% num)

# print("popitem 실행 결과 => ", end="")
# print(num.popitem())
# print("popitem() 후 num : %s"% num)

# info={}; pe=[];bl=True; num=0
# while bl:
#     print("1.인적사항 등록");print("2.검색");print('3.종료')
#     num=int(input(">>>"))
#     if num == 1 :
#         pe.append(input("이름 입력 : ")); pe.append(input("점수 입력 : "))
#         info[pe[0]]=pe[1]
#     elif num == 2:
#         name=input("찾고자하는 학생 이름 입력 : ")
#         if info.get(name) == None: print("찾고자하는 학생이 없습니다.")
#         else:   print(name,"님 점수 : ", info.get(name))
#     elif num==3 :
#         print("프로그램을 종료합니다.")
#         bl=False
#     pe.clear()

# names={'허준','신사임당','권율','홍길동','허준'}

# print(type(names))
# print(len(names))
# print(names)

# s=set({})
# print(type(s))

# print(set('programming'))
# print(set([12,15,17,11,15])) # 0~255 미만 숫자는 위치 고정

# dic={'a':1, 'b':2, 'c':3}
# print(set(dic))

# for x in {'가','나','다','라'}:
#     print(x)

# asia={'korea','china','japan'}
# print(asia)

# asia.add('thailand')
# print(asia)
# asia.add('china')
# print(asia)
# asia.remove('japan')

# print(asia)

# asia={'korea','china','japan'}
# print(asia)
# asia2={'iraq','singapore','korea'}
# asia.update(asia2)
# print(asia)

# print('-'*40)

# asia={'korea','china','japan'}
# asia2={'lraq','singapore','korea'}
# # asia3=asia+asia2
# print(asia3)

# two={2,4,6,8,10,12}
# three={3,6,9,12,15}
# print('교집합',two&three)
# print(two.intersection(three))
# print('합집합',two|three)
# print(two.union(three))
# print('차집합',two-three)
# print(two.difference(three))
# print('배타적 차집합',two^three)
# print(two.symmetric_difference(three))

# animal={'호랑이','사자','강아지','치타','햄스터','고양이'}
# pet={'강아지','고양이','햄스터'}

# print(pet <= animal)
# print(pet <= pet)

# print(pet < animal)
# print(pet < pet)