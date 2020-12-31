'''
https://youtube.com/watch?v=kWiCuklohdY
파이썬 코딩 무료 강의의 내용을 바탕으로 연습
'''

# function
def ex_1():
    def open_account():
        print("새로운 계좌가 생성되었습니다.")

    open_account()

# argument, return
def ex_2():
    def open_account():
        print("새로운 계좌가 생성되었습니다.")

    def deposit(balance, money):
        print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
        return balance + money

    def withdraw(balance, money):
        if balance >= money:
            print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
            return balance - money
        else:
            print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
            return balance

    def withdraw_night(balance, money):
        commission = 100
        if balance >= money + commission:
            print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance - money - commission))
            return balance - money - commission
        else:
            print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
            return balance


    balance = 0
    money = 1000
    balance = deposit(balance, money)
    balance = withdraw_night(balance, 500)

# default
def ex_3():
    def profile(name, age = 17, main_lang = "파이썬"):
        print("이름 : {0}\t나이 : : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

    profile("유재석", 20, "파이썬")
    profile("김태호", 25, "자바")
    profile("정형돈")
    profile("노홍철", 30)

# keyword
def ex_4():
    def profile(name, age, main_lang):
        print(name, age, main_lang)

    profile(name="유재석", main_lang="Java", age=20)

# variable argument
def ex_5():
    '''
    # bad example
    def profile(name, age, lang1, lang2, lang3, lang4, lang5):
        print("이름 : {0}\t나이 : : {1}".format(name, age), end=" ")
        print(lang1, lang2, lang3, lang4, lang5)

    profile("유재석", 20, "python", "java", "C", "C++", "C#")
    profile("김태호", 25, "Kotlin", "Swift", "", "", "")
    '''

    def profile(name, age, *language):
        print("이름 : {0}\t나이 : : {1}".format(name, age), end=" ")
        for lang in language:
            print(lang, end=' ')
        print()

    profile("유재석", 20, "python", "java", "C", "C++", "C#", "JavaScript")
    profile("김태호", 25, "Kotlin", "Swift")

# local / global variable
def ex_6():
    gun = 10
    def checkpoint(soldiers):
        global gun   # global variable
        gun = gun - soldiers    # 바로 위의 문장이 없다면 여기서 gun은 local variable
        print("[함수 내] 남은 총 : {0}".format(gun))

    def checkpoint_ret(gun, soldiers):
        gun = gun - soldiers
        print("[함수 내] 남은 총 : {0}".format(gun))
        return gun

    gun = checkpoint_ret(gun, 2)
    print("전체 총 : {0}".format(gun))

# quiz_1
def quiz_1():
    def std_weight(height, gender):
        if gender == 'M' or gender == 'm':
            print("키 %dcm 남자의 표준 체중은 %.2fkg 입니다." % (height*100, height*height*22))
        else:
            print("키 %dcm 여자의 표준 체중은 %.2fkg 입니다." % (height*100, height*height*21))

    height_1 = 1.75
    gender_1 = 'M'
    std_weight(height_1, gender_1)

    height_2 = 1.60
    gender_2 = 'F'
    std_weight(height_2, gender_2)

import sys
# standard I/O
def ex_7():
    print("Python", "Java", "JavaScript", sep=", ", end="? ")    # print에서 sep, end
    print("무엇이 더 재밌을까요?")

    print("Python", "Java", file=sys.stdout)
    print("Python", "Java", file=sys.stderr)    # buffer에 의해 err가 먼저 시행될 수 있음

    scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
    for subject, score in scores.items():
        print(subject.ljust(8), str(score).rjust(4), sep=":")    # str.ljust(n) / str.rjust(n) -> n칸의 공간에서 왼쪽/오른쪽 정렬을 함

    for num in range(1, 21):
        print("대기번호 : " + str(num).zfill(3))    # str.zfill(n) -> n칸에 대해서 남는 빈 공간을 모두 0으로 채움

    answer = input("아무 값이나 입력하세요 : ")    # 사용자 입력을 통해 값을 받으면 항상 문자열 형태
    print(type(answer))
    print("입력하신 값은 " + answer + "입니다.")

# I/O format
def ex_8():
    print("{0: >10}".format(500))      # :( )> -> 빈공간 공백으로, (>) -> 오른쪽 정렬, (10) -> 10자리 공간 확보
    print("{0: >+10}".format(500))     # 위의 조건 + 양수인 경우 앞에 + 붙임
    print("{0: >+10}".format(-500))    # 위의 조건 + 음수인 경우 앞에 - 붙임

    print("{0:_<+10}".format(500))      # :(_)< -> 빈공간 _로 채움, (<) -> 왼쪽 정렬, (10) -> 10자리 공간 확보, 부호 표시

    print("{0:,}".format(100000000))    # :(,) -> 세자리마다 콤마
    print("{0:+,}".format(100000000))   # +(,) -> 세자리마다 콤마, 부호 표시
    print("{0:^<+30,}".format(100000000)) # +(,) -> 세자리마다 콤마, 자릿수 확보, 부호 표시, 빈자리는 ^ 표시, 왼쪽 정렬

    print("{0:f}".format(5/3))
    print("{0:.2f}".format(5/3))

# File I/O
def ex_9():
    # 특정 설정이 없는 경우 파일의 위치는 .py파일이 실행되는 위치
    '''
    # w 는 write
    score_file = open("score.txt", "w", encoding="utf8")
    print("수학 : 0", file=score_file)
    print("영어 : 50", file=score_file)
    score_file.close()
    '''

    '''
    # a 는 append
    score_file = open("score.txt", "a", encoding="utf8")
    score_file.write("과학 : 80\n")
    score_file.write("코딩 : 100")
    score_file.close()
    '''
    '''
    # r 는 read
    score_file = open("score.txt", "r", encoding="utf8")
    #print(score_file.read())    # 한 번에 모든 내용 다 읽기
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")
    score_file.close()
    '''

    '''
    # line의 개수를 모르는 경우
    score_file = open("score.txt", "r", encoding="utf8")
    while True:
        line = score_file.readline()
        if not line:
            break
        print(line, end="")
    score_file.close()
    '''

    '''
    # list로 모든 내용을 저장하고 싶은 경우
    score_file = open("score.txt", "r", encoding="utf8")
    lines = score_file.readlines()    # list 형태로 저장
    for line in lines:
        print(line, end='')
    score_file.close()
    '''

import pickle
# pickle
# 가지고 있는 데이터를 특정 파일에 저장하고 다시 불러와 활용하도록 도와주는 라이브러리
def ex_10():
    '''
    profile_file = open("profile.pickle", "wb")
    profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
    print(profile)
    pickle.dump(profile, profile_file)
    profile_file.close()
    '''

    '''
    profile_file = open("profile.pickle", "rb")
    profile = pickle.load(profile_file)
    print(profile)
    profile_file.close()
    '''

# with
def ex_11():
    with open("profile.pickle", "rb") as profile_file:
        print(pickle.load(profile_file))

    # with를 활용하는 경우 autoclose 해주므로 close할 필요 없음

    with open("study.txt", "w", encoding="utf8") as study_file:
        study_file.write("파이썬을 공부하고 있어요")

    with open("study.txt", "r", encoding="utf8") as study_file:
        print(study_file.read())

# quiz_2
def quiz_2():
    for i in range(1, 51):
        file_name = str(i) + "주차.txt"
        with open(file_name, "w", encoding="utf8") as report:
            report.write("- " + str(i) + "주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : ")


# execute example
if __name__ == "__main__":
    #ex_11()             # ex_1 ~ ex_11
    #quiz_2()            # quiz_1 ~ quiz_2
    # pass                # pass는 지우고 실행
