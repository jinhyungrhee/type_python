"""
* [composition] : 구성, 분할
* 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않은 경우 사용!
* 유지보수성이 더욱 견고한 소프트웨어를 만들기 위해 사용!
* 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 함
* 2. 부모 클래스의 메서드를 오버라이딩하는 경우, 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Robot:

    """
    [Robot Class]
    Author : 홍길동
    Role : ?????
    """

    __population = 0

    # 생성자
    def __init__(self, name, age):
        self.__name = name  # private 인스턴스 변수
        self.__age = age  # private 인스턴스 변수
        Robot.__population += 1

    # getter
    @property
    def name(self):
        return f"yoon's {self.__name}"

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        else:
            self.__age = new_age

    def say_hi(self):
        self.cal_add(1, 3)  # cal_add()가 여러 함수 내부에 여기저기 쓰이고 있는 경우 유지보수 어려움!
        print(f"Greetings, my master call me {self.name}.")

    # cal_add에 + 1 하나만 추가해도 전부 다 수정되기 때문에 유지보수에 어려움이 생김!
    def cal_add(self, a, b):
        return a + b + 1

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        return f"we have {cls.population} robots."


# 상속(다형성) : polymorphism
class Siri(Robot):
    def say_apple(self):
        print("hello my apple!")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕 사과!")


class Bixby(Robot):
    def say_samsung(self):
        print("hello my samsung")


class BixbyKo(Robot):
    def say_samsung(self):
        print("안녕 삼성")


# composition 사용 (상속X)
class BixbyCal:

    # Robot 전체를 가져오지 않고 특정 메서드만 가져옴 -> composition
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
