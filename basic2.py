'''
https://youtube.com/watch?v=kWiCuklohdY
파이썬 코딩 무료 강의의 내용을 바탕으로 연습
'''

# list
# 값을 한 개씩 반복 가능한 형태로 저장하고 값의 삽입, 수정, 삭제가 자유로움
def ex_1():
    subway = [10, 20, 30]    # list 내에는 아무 원소나 넣을 수 있음
    print(subway)

    subway = ['유재석', '조세호', '박명수']
    print(subway)

    print(subway.index('조세호'))    # list.index(value) -> 찾는 값 index 반환, 없는 경우 error 발생

    subway.append('하하')    # list.append(value) -> 항상 맨 뒤에 삽입
    print(subway)

    subway.insert(1, '정형돈')    # list.insert(index, value) -> 원하는 장소에 삽입
    print(subway)

    print(subway.pop())    # list.pop() -> 맨 뒤의 원소를 삭제
    print(subway)

    print(subway.pop(1))    # list.pop(index) -> index의 원소를 삭제
    print(subway)

    subway.append('유재석')
    print(subway.count('유재석'))    # list.count(value) -> list에 value가 몇 개 들었는지 반환

    num_list = [5,12,3,41,2]
    a = sorted(num_list)  # sorted(list) -> list를 sort하여 sort된 list를 반환 (기존의 list는 그대로 유지)
    print(a)
    num_list.sort()    # list.sort() -> list 그 자체를 sort함
    print(num_list)

    num_list2 = [5,2,3,51,6]
    print(num_list2)
    num_list2.reverse()    # list.reverse() -> list 그 자체를 순서를 뒤집음
    print(num_list2)

    num_list.clear()    # list.clear() -> list 내부에 원소 모두 지움
    print(num_list)

    mix_list = ['조세호', 20, True]    # list는 여러 종류의 원소 가질 수 있음
    num_list = [1,2,3,4,5]
    print(mix_list)
    num_list.extend(mix_list)    # list.extend(another list) -> list는 서로 합칠 수 있음
    print(num_list)

# dictionary
# 값을 {key, value}쌍으로 저장하고 값의 삽입, 삭제, 수정이 자유로움
def ex_2():
    cabinet = {3 : '유재석', 100 : '김태호'}
    print(cabinet[3])
    print(cabinet.get(100))

    # print(cabinet[5])        # 이 방식을 이용하는 경우 key가 없을 때 프로그램이 error가 나면서 종료
    # print(cabinet.get(5))    #이 방식을 이용하는 경우 key가 없을 때 None을 반환

    print(cabinet.get(5, "사용가능"))    # dictionary.get(key, "~")을 통해 key 값이 존재하지 않는 경우 반환 값 설정 가능

    print(3 in cabinet)    # key가 존재하는지 확인가능
    print(5 in cabinet)

    cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
    print(cabinet["A-3"])

    cabinet["C-20"] = "조세호"    # dictionary에 새로운 key-value 쌍을 삽입
    cabinet["A-3"] = "김종국"     # dictionary에 존재하는 key에 새로운 값을 할당하면 기존 값 삭제
    print(cabinet)

    del cabinet["A-3"]    # del dictionary[key]를 통해 dictionary에서 키-값 쌍을 삭제
    print(cabinet)

    print(cabinet.keys())      # key 들만 출력
    print(cabinet.values())    # value들만 출력
    print(cabinet.items())     # key, value쌍 출력

    cabinet.clear()    # 모든 cabinet 비우기
    print(cabinet)

# tuple
# 값을 한 개씩 반복 가능한 형태로 저장하고 한 번 생성된 튜플은 바꿀 수 없음
def ex_3():
    menu = ("돈까스", "치즈까스")
    print(menu[0])
    print(menu[1])

    print(menu.index('돈까스'))      # tuple.index(value)를 통해 index를 구할 수 있음
    print(menu.count('치즈까스'))     # tuple.count(value)를 통해 value의 개수를 구할 수 있음

# set
# 순서 없이 원소들을 관리, 수학의 집합과 같은 형태, 값의 삽입, 삭제 가능
def ex_4():
    my_set = {1,2,3,3,3}
    print(my_set)

    java = {"유재석", "김태호", "양세형"}
    python = set(['유재석', '박명수'])

    print(java & python)                # intersection
    print(java.intersection(python))    # intersection

    print(java | python)         # union
    print(java.union(python))    # union

    print(java - python)              # difference
    print(java.difference(python))    # difference

    python.add("김태호")     # set.add(value)를 통해 값 추가
    print(python)

    java.remove("김태호")    # set.remove(value)를 통해 값 삭제
    print(java)

# list, tuple, dictionary, set
def ex_5():
    menu = {'커피', '우유', '주스'}
    print(menu, type(menu))

    menu = list(menu)
    print(menu, type(menu))

    menu = tuple(menu)
    print(menu, type(menu))

from random import *
# quiz_1
def quiz_1():
    id = list(range(1, 21))
    shuffle(id)    # shuffle(list)를 통해 list를 섞을 수 있음
    winner = sample(id, 4)    # sample(list, n)을 통해 list에서 n개의 sample을 뽑을 수 있음
    print("치킨 당첨자 : " + str(winner[0]))
    print("커피 당첨자 : " + str(winner[1:]))

# if
def ex_6():
    weather = input("오늘 날씨는 어때요? ")
    if weather == '비' or weather == '눈':
        print('우산을 챙기세요.')
    elif weather == '미세먼지':
        print('마스크를 챙기세요.')
    else:
        print('날씨가 괜찮습니다.')

    temp = int(input("기온은 어때요? "))
    if temp >= 30:
        print('너무 더워요. 나가지 마세요.')
    elif temp < 30 and temp >= 10:
        print('괜찮은 날씨에요.')
    elif temp < 10 and temp >= 0:
        print('외투를 챙기세요.')
    else:
        print("너무 추워요. 나가지 마세요.")

# for
def ex_7():
    for waiting_no in [1,2,3,4]:
        print("대기번호 : {0}".format(waiting_no))

    for i in range(1, 5):
        print("대기번호 : " + str(i))

    starbucks = ['아이언맨', '토르', '아이엠 그루트']
    for customer in starbucks:
        print("{0}, 커피가 준비되었습니다.".format(customer))

# while
def ex_8():
    customer = '토르'
    index = 5
    while index >= 1:
        print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
        index -= 1
        if index == 0:
            print("커피는 폐기처분 되었습니다.")

    '''
    # (무한루프)
    while True:
        print("{0}, 커피가 준비 되었습니다.".format(index))
        index += 1
    '''

    customer = "토르"
    person = "Unknown"
    while person != customer:
        print("{0}, 커피가 준비 되었습니다.".format(customer))
        person = input("이름이 무엇인가요? ")

# continue, break
def ex_9():
    absent = [2, 5]
    no_book = [7]
    for student in range(1, 11):
        if student in absent:
            continue
        elif student in no_book:
            print("수업 그만. {0}은 교무실로 따라와.".format(student))
            break
        print("{0}, 책을 읽어봐.".format(student))

# one line for
def ex_10():
    students = [1,2,3,4,5]
    print(students)
    students = [i+100 for i in students]
    print(students)

    students = ['Iron man', 'Thor', 'I am groot']
    students = [len(i)for i in students]
    print(students)

    students = ['Iron man', 'Thor', 'I am groot']
    students = [i.upper() for i in students]
    print(students)

# quiz_2
def quiz_2():
    count = 0

    for i in range(1, 51):
        time = randrange(5, 51)
        if 5 <= time and time <= 15:
            print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
            count += 1
        else:
            print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

    print("총 탑승 승객 :" + count)


# execute example
if __name__ == "__main__":
    #ex_10()             # ex_1 ~ ex_10
    #quiz_2()            # quiz_1 ~ quiz_2
    pass                 # pass는 지우고 실행
