'''
https://youtube.com/watch?v=kWiCuklohdY
파이썬 코딩 무료 강의의 내용을 바탕으로 연습

다른 언어들은 {}를 통해 함수나 클래스를 구분하지만,
파이썬은 띄어쓰기를 통해 함수나 클래스를 구분하므로 띄어쓰기에 유의해야 함
'''

# print
def ex_1():
    print('Hello!')
    print('Hello', 'world!', sep=', ', end = '\n')    # sep는 '', ''에서 '' '' 사이를 연결 / end는 마지막에만 적용
    print('a' + 'b')                                  # '*' + '*' 는 중간에 space가 없음
    print('a', 'b')                                   # '*' , '*' 는 중간에 space가 자동으로 삽입
                                                      # 이를 조작하고 싶으면 print의 인자에 sep, end를 적절히 활용

# type
def ex_2():
    print(type(1))
    print(type(3.14))
    print(type('Hello!'))
    print(type(True))

# variables
def ex_3():
    animal = "강아지"
    name = "뽀삐"
    age = 4
    is_adult = age >= 3

    print("우리집 " + animal + "의 이름은 " + name + "예요")
    print(name + "의 나이는 " + str(age) + "살이예요")
    print(name + "은 어른인가요? " + str(is_adult))

# comments
def ex_4():
    # 이 문장은 주석으로 실행되지 않음
    '''
    이렇게 3개의 작은 따옴표를 이용하여 여러 줄 주석 처리할 수 있음
    '''

# quiz_1
def quiz_1():
    station = ['사당', '신도림', '인천공항']
    for i in station:
        print(i + "행 열차가 들어오고 있습니다.")

# operator 1 (calculation)
def ex_5():
    print(1 + 1)
    print(3 - 2)
    print(5 * 2)
    print(5 / 3)
    print(2 ** 3)
    print(5 // 3)
    print(5 % 3)
    print(10 > 3)
    print(5 >= 7)
    print(3 == 3)

# operator 2 (compare)
def ex_6():
    print(1 != 3)
    print(not(1 != 3))
    print((3 > 0) and (3 < 5))
    print((3 > 0) & (3 < 5))
    print((3 > 0) or (3 > 5))
    print((3 > 0) | (3 > 5))

    # lazy evaluation
    # 만약 and 연산을 할 때 첫 값이 False면 뒤의 연산 수행 x
    # 만약 or 연산을 할 때 첫 값이 True면 뒤의 연산 수행 x

# expression
def ex_8():
    print(2 + 3 * 4)
    print((2 + 3) * 4)
    number = 10
    print(number)
    number += 12    # +=, -=, *=, /= 으로 응용 가능
    print(number)

# number function
from math import *
def ex_9():
    # no need to import math
    print(abs(-5))
    print(pow(4, 2))
    print(max(5, 12))
    print(min(5, 12))
    print(round(3.14))
    print(round(4.99))

    # need to import math
    print(floor(4.99))
    print(ceil(3.14))
    print(sqrt(16))    # return type is float

# random
from random import *
def ex_10():
    print(random())              # [0, 1) 사이의 임의의 값 생성 (float)
    print(random() * 10)         # [0, 10) 사이의 임의의 값 생성 (float)
    print(int(random() * 10))    # [0, 10) 사이의 임의의 값 생성 (int)

    print(randrange(1, 10))      # [1, 10) 사이의 임의의 값 생성 (int)
    print(randint(1, 10))         # [1, 10] 사이의 임의의 값 생성 (int)

# quiz_2
def quiz_2():
    a = randint(4, 28)
    print("오프라인 스터디 모임 날짜는 매월 " + str(a) + "일로 선정되었습니다.")

# string
def ex_11():
    sentence = "나는 사람입니다."
    print(sentence)
    sentence1 = """나는 사람입니다.
파이썬은 쉽습니다."""
    print(sentence1)

# slicing  [시작점(포함) : 종료점(미포함) : 간격]
def ex_12():
    code = "990120-1234567"
    print("성별 : 남" if int(code[7]) == 1 else "성별 : 여")    # (참) if (조건문) else (거짓) 의 형태로 한 줄 if else 가능
    print("나이 : " + str(21 - int(code[0:2])) if int(code[0:2]) <= 20 else "나이 : " + str(121 - int(code[0:2])))
    print("월 : " + code[2:4])
    print("일 : " + code[4:6])
    print("생년월일 : " + code[:6])
    print("뒷자리 : " + code[-7:])    # 파이썬은 음의 인덱싱을 지원

# string function
def ex_13():
    python = "Python is Amazing"
    print(python.lower())                      # 모든 문자를 소문자로 표현
    print(python.upper())                      # 모든 문자를 대문자로 표현
    print(python[0].isupper())                 # 대문자인지 확인후 bool 반환
    print(len(python))                         # 문자열 길이 반환
    print(python.replace("Python", "Java"))    # 문자열을 치환 (바꿀 문자열, 바꿔질 문자열)

    index = python.index('n')                  # 찾는 문자 혹은 문자열 시작 위치 반환
    print(index)
    index = python.index('n', index + 1)       # 그 다음 문자열을 찾기 위해서 다음 방법 사용 가능
    print(index)                               # 함수 전달 인자는 (찾는 문자열, (시작 위치), (종료 위치))로 구성

    print(python.find('n'))                    # index, find의 작동 방식은 동일, 함수 전달 인자도 동일 구성
    print(python.find('Java'))                 # index, find의 차이점은 찾는 문자열이 없는 경우 index는 error 발생 / find는 -1을 return

# string format
def ex_14():
    # way1 (%)
    print("나는 %d살 입니다." % 20)    # %d %f %c %s를 활용하여 printf 처럼 활용할 수 있음
    print("나는 %s를 좋아해요." % "파이썬")
    print("Apple는 %c로 시작해요." % 'A')
    print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))    # %뒤의 괄호는 tuple 형태이어야 함

    # way2 ({} .format)
    print("나는 {}살 입니다.".format(20))
    print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))    # 문자열.format((tuple))의 형태 이어야 함
    print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))

    # way 3 ({} .format(variable = (value)))
    print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))

    # way 4 (f {})
    age = 20
    color = "빨강"
    print(f"나는 {age}살이며, {color}색을 좋아해요.")

# string additional
def ex_15():
    print("백문이\n불여일견")        # \n 줄바꿈
    print("저는 \"사람\"입니다.")    # \ 따옴표를 출력
    print("\\")                     # \\ 역슬래시 출력
    print("Red Apple\rPine")        # \r 캐리지 리턴 -> 커서를 맨 앞으로 이동 덮어쓰기 (Mac / Window에 따라 차이 있을 수 있음)
    print("Redd\bApple")            # \b 백스페이스 -> 한 글자 삭제
    print("Rde\tApple")             # \t 탭 -> 탭과 동일한 효과

# quiz_3
def quiz_3():
    site = "http://youtube.com"
    my_str = site.replace("http://", "")
    my_str = my_str[:my_str.index(".")]
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + '!'
    print("생성된 비밀번호 : " + password)


# execute example
if __name__ == "__main__":
    # ex_15()             # ex_1 ~ ex_15
    # quiz_3()            # quiz_1 ~ quiz_3
    #pass                 # pass는 지우고 실행
