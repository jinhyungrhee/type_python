"""
* [property]
* 1.인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
* 2.인스턴스 변수 값에 대한 유효성 검사 및 수정
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

    # 사용 예제1
    @property
    def name(self):
        return f"yoon's {self.__name}"

    # 사용 예제2
    # @property 데코레이터(=getter)
    # __age라는 private 변수에 접근(읽기) 가능하도록 함
    @property
    def age(self):
        return self.__age

    # @프로퍼티명.setter 데코레이터(=setter)
    # __age라는 private 변수를 변경(쓰기) 가능하도록 함
    # 외부에서 직접 변경하지 못하고, setter 함수를 이용하여 간접적으로만 변경 가능하도록 설정!
    @age.setter
    def age(self, new_age):
        # 이상한 값 예외 처리
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


droid = Robot("R2-D2", 2)

# ======================== getter ============================
# 직접 접근(읽기) 불가
# print(droid.__age)
"""
AttributeError: 'Robot' object has no attribute '__age'
"""
# property 데코레이터로 private 변수 접근(=getter)
print(droid.age)
"""
2
"""

# ====================== setter ===============================
# 직접 접근(쓰기) 불가
# droid.age = 77
"""
AttributeError: can't set attribute
"""
# @프로퍼티명.setter 데코레이터로 private 변수 접근(=setter)
droid.age = 7
print(droid.age)
"""
7
"""

droid.age += 1
print(droid.age)
"""
8
"""

# 은닉(encapsulation) 사용 이유
# 특정 사용자가 이상한 값을 집어넣을 경우, setter 함수 내부에서 예외처리 가능!
# droid.age = -999
"""
TypeError: invalid range to age
"""

print(droid.name)
"""
yoon's R2-D2
"""
