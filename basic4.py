'''
https://youtube.com/watch?v=kWiCuklohdY
파이썬 코딩 무료 강의의 내용을 바탕으로 연습
'''

# class
def ex_1():
    '''
    # bad
    name = "마린"
    hp = 40
    damage = 5

    print("{} 유닛이 생성되었습니다.".format(name))
    print("체력 {0}, 공격력 {1}\n".format(hp, damage))

    tank_name = "탱크"
    tank_hp = 150
    tank_damage = 35

    print("{} 유닛이 생성되었습니다.".format(tank_name))
    print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

    def attack(name, location, damage):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

    attack(name, "1시", damage)
    attack(tank_name, "1시", tank_damage)
    '''

    class Unit:
        def __init__(self, name, hp, damage):    # 생성자
            self.name = name
            self.hp = hp
            self.damage = damage
            print("{0} 유닛이 생성 되었습니다.".format(self.name))
            print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    marine1 = Unit("마린", 40, 5)
    marine2 = Unit("마린", 40, 5)
    tank = Unit("탱크", 150, 35)
    wraith1 = Unit("레이스", 80, 5)
    print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

    wraith2 = Unit("레이스", 80, 5)
    wraith2.clocking = True

    if wraith2.clocking == True:
        print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# method
def ex_2():
    class Unit:
        def __init__(self, name, hp, damage):    # 생성자
            self.name = name
            self.hp = hp
            self.damage = damage
            print("{0} 유닛이 생성 되었습니다.".format(self.name))
            print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    class AttackUnit:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

    firebat1 = AttackUnit("파이어뱃", 50, 16)
    firebat1.attack("5시")
    firebat1.damaged(25)
    firebat1.damaged(25)

# inheritance
def ex_3():
    class Unit:    # parant class
        def __init__(self, name, hp):    # 생성자
            self.name = name
            self.hp = hp
            print("{0} 유닛이 생성 되었습니다.".format(self.name))

    class AttackUnit(Unit):    # children class
        def __init__(self, name, hp, damage):
            Unit.__init__(self, name, hp)
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

    firebat1 = AttackUnit("파이어뱃", 50, 16)
    firebat1.attack("5시")
    firebat1.damaged(25)
    firebat1.damaged(25)

# multiple inheritance
def ex_4():
    class Unit:
        def __init__(self, name, hp):    # 생성자
            self.name = name
            self.hp = hp
            print("{0} 유닛이 생성 되었습니다.".format(self.name))

    class AttackUnit(Unit):
        def __init__(self, name, hp, damage):
            Unit.__init__(self, name, hp)
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

    class Flyable:
        def __init__(self, flying_speed):
            self.flying_speed = flying_speed

        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

    class FlyableAttackUnit(AttackUnit, Flyable):
        def __init__(self, name, hp, damage, flying_speed):
            AttackUnit.__init__(self, name, hp, damage)
            Flyable.__init__(self, flying_speed)

    valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
    valkyrie.fly(valkyrie.name, "3시")

# method overridding
def ex_5():
    class Unit:
        def __init__(self, name, hp, speed):    # 생성자
            self.name = name
            self.hp = hp
            self.speed = speed

        def move(self, location):
            print("[지상 유닛 이동]")
            print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    class AttackUnit(Unit):
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

    class Flyable:
        def __init__(self, flying_speed):
            self.flying_speed = flying_speed

        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

    class FlyableAttackUnit(AttackUnit, Flyable):
        def __init__(self, name, hp, damage, flying_speed):
            AttackUnit.__init__(self, name, hp, 0, damage)
            Flyable.__init__(self, flying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)


    valture = AttackUnit("벌쳐", 80, 10, 20)
    battlecrusier = FlyableAttackUnit("배틀크루져", 500, 25, 3)

    #valture.move("11시")
    #battlecrusier.fly(battlecrusier.name, "9시")

    valture.move("11시")
    battlecrusier.move("9시")    # method overriding을 통해서 부모 클래스와 같은 함수를 자식 클래스에서 다른 동작을 하도록 조작

# pass
def ex_6():
    class Unit:
        def __init__(self, name, hp, location):    # 생성자
            self.name = name
            self.hp = hp
            self.location = location

    class BuildingUnit(Unit):
        def __init__(self, name, hp, location):
            pass    # 나중에 구현 하기 위해 내버려 둠. 아무 일도 하지 않음.

    supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

    def game_start():
        print("[알림] 새로운 게임을 시작합니다.")

    def game_over():
        pass

    game_start()
    game_over()

# super
def ex_7():
    '''
    # super().__init__() 사용법
    class Unit:
        def __init__(self, name, hp, speed):    # 생성자
            self.name = name
            self.hp = hp
            self.speed = speed

    class BuildingUnit(Unit):
        def __init__(self, name, hp, location):
            #Unit.__init__(self, name, hp, 0)
            super().__init__(name, hp, 0)    # super()를 통해서 부모 클래스에 대한 초기화를 진행할 때는 self 인자를 보내지 않음
            self.location = location
    '''

    class Unit:
        def __init__(self):
            print("Unit 생성자")

    class Flyable:
        def __init__(self):
            print("Flyable 생성자")

    class FlyableUnit(Unit, Flyable):
        def __init__(self):
            # super().__init__()    # super().__init__()은 먼저 상속 받는 것에 대해서 초기화
            Unit.__init__(self)
            Flyable.__init__(self)

    dropship = FlyableUnit()

from random import *
# starcraft
def ex_8():
    class Unit:
        def __init__(self, name, hp, speed):
            self.name = name
            self.hp = hp
            self.speed = speed
            print("{0} 유닛이 생성되었습니다.".format(self.name))

        def move(self, location):
            print("[지상 유닛 이동]")
            print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

    class AttackUnit(Unit):
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    class Flyable:
        def __init__(self, flying_speed):
            self.flying_speed = flying_speed

        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

    class FlyableAttackUnit(AttackUnit, Flyable):
        def __init__(self, name, hp, damage, flying_speed):
            AttackUnit.__init__(self, name, hp, 0, damage)
            Flyable.__init__(self, flying_speed)

        def move(self, location):
            print("[공중 유닛 이동]")
            self.fly(self.name, location)

    class Marine(AttackUnit):
        def __init__(self):
            AttackUnit.__init__(self, "마린", 40, 1, 5)

        def stimpack(self):
            if self.hp > 10:
                self.hp -= 10
                print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
            else:
                print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

    class Tank(AttackUnit):
        seize_developed = False    # 전체 Tank class에 대한 variable

        def __init__(self):
            AttackUnit.__init__(self, "탱크", 150, 1, 35)
            self.seize_mode = False

        def set_seize_mode(self):
            if Tank.seize_developed == False:  # 전체 Tank 클래스들에 대해 클래스 변수 seize_developed
                return

            if self.seize_mode == False:
                print("{0} : 시즈모드로 전환합니다.".format(self.name))
                self.damage *= 2
                self.seize_mode = True
            else:
                print("{0} : 시즈모드를 해제합니다.".format(self.name))
                self.damage /= 2
                self.seize_mode = False

    class Wraith(FlyableAttackUnit):
        def __init__(self):
            FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
            self.clocked = False

        def clocking(self):
            if self.clocked == True:
                print("{0} : 클로킹 모드 해제합니다.".format(self.name))
                self.clocked = False
            else:
                print("{0} : 클로킹 모드 설정합니다.".format(self.name))
                self.clocked = True

    def game_start():
        print("[알림] 새로운 게임을 시작합니다.")

    def game_over():
        print("Player : gg")
        print("[Player] 님이 게임에서 퇴장하셨습니다.")

    game_start()

    m1 = Marine()
    m2 = Marine()
    m3 = Marine()

    t1 = Tank()
    t2 = Tank()

    w1 = Wraith()

    attack_units = []
    attack_units.append(m1)
    attack_units.append(m2)
    attack_units.append(m3)
    attack_units.append(t1)
    attack_units.append(t2)
    attack_units.append(w1)

    for unit in attack_units:
        unit.move("1시")

    Tank.seize_developed = True
    print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

    for unit in attack_units:
        if isinstance(unit, Marine):    # isinstance(instance, class) 특정 instance가 class의 인스턴스인지 확인하는 method
            unit.stimpack()
        elif isinstance(unit, Tank):
            unit.set_seize_mode()
        elif isinstance(unit, Wraith):
            unit.clocking()

    for unit in attack_units:
        unit.attack("1시")

    for unit in attack_units:
        unit.damaged(randint(5, 21))

    game_over()

# quiz_1
def quiz_1():
    class House:
        def __init__(self, location, house_type, deal_type, price, completion_year):
            self.location = location
            self.house_type = house_type
            self.deal_type = deal_type
            self.price = price
            self.completion_year = completion_year

        def show_detail(self):
            print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

    gan_apt = House("강남", "아파트", "매매", "10억", "2010년")
    map_off = House("마포", "오피스텔", "전세", "5억", "2007년")
    song_vil = House("송파", "빌라", "월세", "500/50", "2000년")

    house_list = []
    house_list.append(gan_apt)
    house_list.append(map_off)
    house_list.append(song_vil)

    print("총 " + str(len(house_list)) + "채의 매물이 있습니다.")
    for house in house_list:
        house.show_detail()


# execute example
if __name__ == "__main__":
    #ex_8()              # ex_1 ~ ex_8
    #quiz_1()            # quiz_1
    #pass                # pass는 지우고 실행
