"""
[magic method]
* Python에서 __xxx__ 형태를 가진 메서드들은 전부 magic method(=built-in method)임!
* 각 magic method들은 역할을 가지고 있음!
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
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1

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

    # 클래스 메서드 (데코레이터 사용)
    @classmethod
    def how_many(cls):
        # cls는 클래스(Robot)를 받는 변수
        return f"we have {cls.population} robots."

    # self나 cls를 사용하지 않는 방법은 없을까? => <<Static Method>>
    @staticmethod
    def this_is_robot_class():
        print("yes!!")

    # str메서드 커스터마이징(=overriding)
    def __str__(self):
        return f"{self.name} robot!!"

    # 실행가능한 객체로 설정
    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


droid1 = Robot("R2-D2")
droid1.say_hi()
print(dir(droid1))
"""
Greetings, my master call me R2-D2.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', 'cal_add', 'die', 'how_many', 'name',
 'population', 'say_hi', 'this_is_robot_class']
"""

# ===================== __str__ =============================================
# print(객체) -> 사용자에게 객체를 어떻게든 보여주기 위해 '문자열화' 시키는 것!
# print(droid1)
"""
<__main__.Robot object at 0x0000020CF88F8BB0>
"""

# 즉, print()를 사용하면 Python 내부적으로 정의된 __str__() 메서드를 호출하는 것임!
# print(droid1.__str__())
"""
<__main__.Robot object at 0x000001FFC9C38BB0>
"""

# 클래스 내에서 str 메서드 커스터마이징한 결과
# : 객체에 대한 __str__메서드를 실행시킨 것!
print(droid1)
"""
R2-D2 robot!!
"""

# ================= __call__ ===============================
# Python에서 모든 것은 '객체'임!
# 함수 또한 특정 클래스로 만들어진 '객체'임!
# ()는 '실행가능한 객체(=callable)'를 의미함

# 이전에 Robot클래스로 만들어진 객체는 실행가능한 객체가 아니므로 () 사용시 에러 발생!
# droid1()
"""
TypeError: 'Robot' object is not callable
"""

# Robot클래스에 __call__ 메서드 추가 후 () 사용하면 정상 동작!
# : 객체가 함수처럼 변화함 -> callable 객체가 되었기 때문!
# : 해당 객체에 __call__이라는 magic method가 정의가 되어 있기 때문!
droid1()
"""
call!
"""
