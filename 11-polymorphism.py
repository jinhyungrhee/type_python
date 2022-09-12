"""
* polymorphism
* 여러 형태를 가질 수 있도록 함. 즉, 객체를 부품화할 수 있도록 함.
* 같은 형태의 코드가 다른 동작을 하도록 하는 것.
* '다형성'을 지키는 코드는 <재사용성>과 <유지보수성>이 우수함!
"""


class Robot:

    """
    [Robot Class]
    Author : 홍길동
    Role : ?????
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
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
        # 예외 처리
        if new_age < 0:
            raise TypeError("invalid range to age")
        else:
            self.__age = new_age

    def say_hi(self):
        print(f"Greetings, my master call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        return f"we have {cls.population} robots."


# 같은 형태의 코드가 서로 다른 의미를 갖도록 함 : 다형성
class Siri(Robot):
    def say_apple(self):
        print("hello my apple!")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요~")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요!")
