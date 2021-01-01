'''
https://youtube.com/watch?v=kWiCuklohdY
파이썬 코딩 무료 강의의 내용을 바탕으로 연습
'''

# try-except
def ex_1():
    try:
        print("나누기 계산")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        print("{} / {} = {}".format(num1, num2, int(num1)/int(num2)))

    except ValueError:
        print("에러! 잘못된 값을 입력하였습니다.")

    except ZeroDivisionError as err:
        print(err)

    except Exception as err:
        print(err)

# raise error
def ex_2():
    try:
        print("한 자리 숫자 나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        if num1 >= 10 or num2 >= 10:
            raise ValueError
        print("{} / {} = {}".format(num1, num2, int(num1)/int(num2)))

    except ValueError:
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# error definition
def ex_3():
    class BigNumberError(Exception):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg


    try:
        print("한 자리 숫자 나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        if num1 >= 10 or num2 >= 10:
            raise BigNumberError("입력값 : {}, {}".format(num1, num2))
        print("{} / {} = {}".format(num1, num2, int(num1)/int(num2)))

    except ValueError:
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

    except BigNumberError as err:
        print("에러가 발생하였습니다. 값이 한 자리 숫자가 아닙니다.")
        print(err)

# finally
def ex_4():
    class BigNumberError(Exception):    # exception class를 상속 받아야 함
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg

    try:
        print("한 자리 숫자 나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        if num1 >= 10 or num2 >= 10:
            raise BigNumberError("입력값 : {}, {}".format(num1, num2))
        print("{} / {} = {}".format(num1, num2, int(num1) / int(num2)))

    except ValueError:
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

    except BigNumberError as err:
        print("에러가 발생하였습니다. 값이 한 자리 숫자가 아닙니다.")
        print(err)

    finally:
        print("계산기를 이용해 주셔서 감사합니다.")

# quiz_1
def quiz_1():
    class SoldOutError(Exception):
        pass

    chicken = 10
    waiting = 1

    while(True):
        try:
            print("[남은 치킨 : {}]".format(chicken))
            order = int(input("치킨 몇 마리 주문하시겠습니까?"))

            if order > chicken:
                print("재료가 부족합니다.")
            elif order <= 0:
                raise ValueError
            else:
                print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
                waiting += 1
                chicken -= order

            if chicken == 0:
                raise SoldOutError

        except ValueError:
            print("잘못된 값을 입력하셨습니다.")

        except SoldOutError:
            print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            break


# execute example
if __name__ == "__main__":
    #ex_4()              # ex_1 ~ ex_4
    #quiz_1()            # quiz_1
    #pass                # pass는 지우고 실행
