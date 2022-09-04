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


droid1 = Robot("R2-D2")
droid1.say_hi()
print(Robot.how_many())

droid2 = Robot("amamov")
droid2.say_hi()
print(Robot.how_many())

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid2.die()
print(Robot.how_many())


"""
* dir() : 모든 속성 값 확인
* __dict__ : 네임스페이스 확인
* __doc__ : class 주석 확인
* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인
"""
print(dir(Robot))
print(dir(droid1))
print(Robot.__doc__)
print(droid1.__class__)

# self나 cls를 사용하지 않는 메서드에 접근하는 방법? => <<Static Method>>
# : self나 cls를 사용하지 않아도 되므로 좀 더 자유롭게 사용가능한 메서드!

# 인스턴스에서 접근1 -> 에러 발생(@staticmethod 데코레이터 추가하지 않을 시)
# print(droid1.this_is_robot_class())
"""
TypeError: this_is_robot_class() takes 0 positional arguments but 1 was given
"""
# 인스턴스에서 접근2 -> 정상동작(@staticmethod 데코레이터 추가 시)
print(droid1.this_is_robot_class())
"""
yes!!
None
"""

# 클래스에서 접근 -> 정상 동작(@staticmethod 데코레이터 추가하든 안하든 정상동작)
print(Robot.this_is_robot_class())
"""
yes!!
None
"""
