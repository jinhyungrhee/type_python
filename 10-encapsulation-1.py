"""
* public vs private
* private : 외부에서 함부로 접근할 수 없도록 설정 (__변수명) -> 특정 변수의 '은닉'
            상속을 받더라도 상속 대상이 private 변수에 접근할 수 없음! (클래스 자체에서만 사용 가능!)
* public : 외부에서 누구나 접근 가능하도록 설정 (__변수명__)
* protect : 상속 대상까지만 접근을 허용하고 그 이외의 사람들에게는 접근을 허용하지 않음.
            Python 커뮤니티에서는 암묵적으로 접근하지 않도록 (_변수명)으로 사용하 -> 접근 못하도록 강제 X
            (= 외부에서도 접근 가능, pulic과 다를게 없음)
* 변수나 메서드 모두 앞에 __를 붙이면 외부에서 접근할 수 없음!(namespace에서 은닉)
"""


class Robot:

    """
    [Robot Class]
    Author : 홍길동
    Role : ?????
    """

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        # self.__age = age  # private 변수
        # self.__age__ = age # public 변수
        self._age = age  # protected 변수(암묵적 rule)
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # business logic
        print(f"Greetings, my master call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 클래스 메서드 (데코레이터 사용)
    @classmethod
    def how_many(cls):
        # cls는 클래스(Robot)를 받는 변수
        return f"we have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        # self.__age = 999
        # print(self.__age)
        print(self._age)


ss = Robot("yss", 8)

# print(ss.age)

# 다른 누군가가 ss의 age를 바꾸는 경우 (namespace가 보호가 안된 상황)
# ss.age = -999

# print(ss.age)

# age를 private 변수로 변경(self.__age)
# print(ss.age)
# print(ss.__age)
"""
AttributeError: 'Robot' object has no attribute 'age'
"""

# protect
ssss = Siri("iphone8", 9)
