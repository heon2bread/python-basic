# be=['2019','12','31'] # 같은 속성이여야 가능
# print(be)

# af=list(map(int,be)) # tuple, set 자료형 지정 함수
# print(af)
# # map 반복문 대치함수

# 시퀀스형 자료형

# tp=(10,20,30)
# print("tp : ", tp)
# print("tp type : ", type(tp))
# print("tp len : ", len(tp))

# tp1=10,20,30
# print("tp1 : ",tp1)
# print("tp1 type :",type(tp1))

# print("tp1[0]type : ",type(tp1[0]))

# tp1[0]=100 # 에러발생 - []안의 값을 교체 불가하기 때문에

# tpType="문자열",100,1.111

# print("tpType : ",tpType)
# print("type : ",type(tpType))
# print("tpType[0] type : ",type(tpType[0]))
# print("tpType[1] type : ",type(tpType[1]))
# print("tpType[2] type : ",type(tpType[2]))

# tplnt=(10)
# print("tplnt : ",type(tplnt)); # <class 'int'>

# tpT1=(10,)
# print("tpT1 : ",type(tpT1)); # <class 'tuple'>

# tpT2=10,
# print("tpT2 : ", type(tpT2)); # <class 'tuple'>

# tt1 = (10, 20, 30, 40)
# tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3]
# print("튜플 합 : %d"% tt2)

# print("tt1[1:3]:",tt1[1:3])
# print("tt1[1:]:",tt1[1:])
# print("tt1[;3]:",tt1[:3])

# a = 1,2,3
# b = 4,5,6
# c = a+b

# print("a : ",a)
# print("b : ",b)
# print("c : ",c)

# ★★( packing & unpacking )★★
# pack = 1,2,"패킹"
# print("packing\npack : ",pack)

# a,b,c=pack # a=b a,b 구성요소 갯수는 같아야 언패킹 가능
# print("unpacking\na:",a,"b:",b,"c",c)

# tp=100,200,"함수",100,'개수'

# print("tp안의 200의 위치:",tp.index(200),'번째 인덱스')
# print("tp만의 100의 개수:",tp.count(100),"개")

# tp = '회사정보','제품명','가격정보','출시일'
# ls = ['삼성전자','갤럭시','100원','미정']
# for i in range(len(tp)):
#     print("%s : %s"%(tp[i],ls[i]))

# 딕셔너리

# student = {'학번':1234, '이름':'홍길동', '학과':'it학과'}
# print(student)

# mobile={"품명":"갤럭시","가격":100,"크기":10}
# print(mobile)

# impo={} # 이름 지정하여 쓸거니까 초기화 할 때 사용
# impo['파이썬']='www.python.org'
# impo['네이버']='www.naver.com'
# impo['구글']='www.google.com'

# print("파이썬:",impo['파이썬'])
# print("네이버:",impo['네이버'])
# print("구글:",impo['구글'])
# print(impo)

# impo={}
# name=input('키값 입력:')
# val=input('값 입력')
# impo[name]=val

# print(name,":",impo[name])
# print(impo)


# 딕셔너리의 키값은 중복 불가
# overwatch={}
# for i in range(5):
#     name=input('캐릭터명 입력:')
#     skill=input('스킬명 입력:')
#     overwatch[name]=skill
# print(overwatch)

# import collections
#순서있는 사전
# overWatch=collections.OrderedDict()
# OrderedDict() 함수는 입력한 순서대로 메모리상의 순서도 고정시켜주는 함수
# 딕셔너리는 데이터를 메모리가 던져주는 순서대로 출력이 됐는데
# 2. 버전대에서 입력된 순서대로 메모리에 순서도 고정해주는 OrderedDict()함수를 사용해서 입력된 순서대로 출력을 하였습니다.
# i=0; name=""; val=""
# for i in range(5):
#     name=input("이름(key)입력 : ")
#     val=input("값(value)입력 : ")
#     overWatch[name]=val
# print(overWatch)

# num={1:"일",2:"이",3:"삼",4:"사"}

# print('keys()키:',num.keys())
# print()
# print('values()값:',num.values())

# num={1:"일",2:"이",3:"삼",4:"사"}

# print("num.keys():",num.keys())
# print("list(num):",list(num))
# print("list(num.keys()):",list(num.keys()))
# print()
# print("num.values():",num.values())
# print("list(num.values()):",list(num.values()))

# singer={}
# singer['이름']=input('가수 이름 입력 : ')
# singer['구성원']=input('구성원 이름 입력 : ')
# singer['대표곡']=input('대표곡 이름 입력 : ')

# for i in singer.keys():
#     print('%s : %s'% (i,singer[i]))
# print(singer)

# menu={}; bl=True; num=0
# while bl:
#     print("1.메뉴등록");print("2.메뉴별 가격보기");print("3.가격 수정");print("4.종료")
#     num=int(input(">>>"))
#     if num == 1:
#         name = input("메뉴 입력 : ");menu[name] = input("가격 입력 : ")
#     elif num==2:
#         for i in menu.keys():
#             print(i,":",menu[i])
#     elif num==3:
#         name=input("수정 할 목록 입력");menu[name] = input("수정 가격 : ")
#     elif num==4:
#         print('프로그램 종료 합니다.')
#         bl=False
# print(bl)
# 버그 수정
menu={}; bl=True; num=0
while bl:
    print("1.메뉴등록");print("2.메뉴별 가격보기");print("3.가격 수정");print("4.종료")
    num=int(input(">>>"))
    if num == 1:
        name = input("메뉴 입력 : ")
        if menu.get(name) != None : print('이미 등록된 메뉴 입니다.')
        else :
            menu[name] = input("가격 입력 : ")
    elif num==2:
        for i in menu.keys():
            print(i,":",menu[i])
    elif num==3:
        name=input("수정 할 목록 입력")
        if menu.get(name) == None : print('등록되지 않은 메뉴입니다.')
        else:
            menu[name] = input("수정 가격 : ")
    elif num==4:
        print('프로그램 종료 합니다.')
        bl=False
print(bl)

# num={1:"일",2:"이",3:"삼",4:"사",5:"오"}

# print(num)
# print("num.get(3):",num.get(3))
# print("num.get(9):",num.get(9))
# print("num.get(0):",num.get(0,'없음')) # .get() 다양한 형태로 반환 가능

# su=int(input("찾고자하는 키 입력 : "))
# if num.get(su)==None:
#     print("값이 없습니다.")
# else:
#     print(num.get(su))