"""
* 추상화 : abstraction
* 불필요한 정보는 숨기고 중요한(필요한) 정보만 표현함
* 공통의 속성, 값, 행위(methods)를 하나로 묶어 이름 붙이는 것
"""
# ================== 추상화O ===========================
# : 공통된 속성을 뽑아내서 하나의 클래스로 만듦


class Robot:
    # 클래스 공간(class namespace)안에 존재하며, 각 instance들이 공유하는 변수와 메서드 => 클래스 변수, 클래스 메서드
    # **클래스 변수** : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수(key-value 쌍으로 저장됨)
        self.code = code  # 인스턴스 변수
        Robot.population += 1  # 클래스 변수

    # 인스턴스 메서드
    def say_hi(self):
        # business logic
        print(f"Greetings, my master call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # **클래스 메서드** => 데코레이터 사용!
    @classmethod
    def how_many(cls):
        # cls는 클래스(Robot)를 받는 변수
        print(f"we have {cls.population} robots.")


# 클래스 변수 사용
print(f"Robot Count : {Robot.population}")
siri = Robot("siri", 210397888)
print(f"Robot Count : {Robot.population}")
jarvis = Robot("jarvist", 123456789)
print(f"Robot Count : {Robot.population}")
bixby = Robot("bixby", 987654321)
print(f"Robot Count : {Robot.population}")
bixby2 = Robot("bixby", 8768464665)
print(f"Robot Count : {Robot.population}")
bixby3 = Robot("bixby", 1664846841)
print(f"Robot Count : {Robot.population}")

# 인스턴스 변수, 인스턴스 메서드 사용
print(siri.name)
print(siri.code)
siri.say_hi()
print(siri.cal_add(2, 3))

# 클래스 메서드 사용
Robot.how_many()

# ================= 추상화X ===========================

# # robot siri
# siri_name = "siri"

# siri_code = "210397888127"


# def siri_say_hi():
#     # skip complex business logic
#     print("say hello! my name is siri!")


# def siri_add_cal():
#     return 2 + 3


# def siri_die():
#     # skip complex business logic
#     print("bye! see you later!")


# # robot jarvis
# jarvis_name = "jarvis"

# jarvis_code = "123456789"

# # ...

# # robot bixby
# bixby_name = "bixby"

# bixby_code = "987654321"

# # ...
