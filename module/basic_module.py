### module ###

# import theater_module
#
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
#
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
#
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
#
# price(5)
# price_morning(6)
# # price_soldier(7) 사용할 수 없음

# from theater_module import price_soldier as price
#
# price(5)


### package ###
# import travel.thailand
# # import travel.thailand.ThailandPackage         -> 이 형태의 class import는 불가능
# # from travel.thailand import ThailandPackage    -> 이 형태의 class import는 가능
#
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
# type(trip_to)    # trip_to는 object 타입
#
# from travel import vietnam
#
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


### __all__ ###
# # __init__ 에서 __all__에 추가를 해주어야 사용가능
# from travel import *
#
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
#
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


### module call ###
# if __name__ == "__main__" 구문을 통해서 모듈 내부 호출을 확인가능
# 다른 py파일에서 호울하는 경우 외부에서 모듈을 호출한 것


### location ###
# import inspect
# import random
# from travel import *
#
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))
#
# # Python x.x\lib 폴더 내에 module을 갖다 놓으면 모듈 인식


### pip install ###
# pip install
# pip list
# pip show
# pip install --upgrade
# pip uninstall


### built-in function ###
# # input
# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋은 언어 입니다!".format(language))
#
# # dir
# print(dir())
#
# import random
# print(dir())
#
# import pickle
# print(dir())
# print(dir(random))
#
# lst = [1,2,3]
# print(dir(lst))
#
# name = "Jim"
# print(dir(name))
#
# # python 공식 문서에서 더 많은 정보 획득 가능


### external function ###
# list python module index

# # glob
# import glob
# print(glob.glob("*.py"))
#
# # os
# import os
# print(os.getcwd())
#
# folder = "sample_dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
#
# print(os.listdir())
#
# # time
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
#
# # datetime
# import datetime
# print("오늘 날짜는", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print(today + td)


### quiz ###
# import byme
# byme.sign()
