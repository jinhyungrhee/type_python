"""
[클래스 상속]
* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속됨
* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있음
* 3. 메서드 오버라이딩
* 4. super()
* 5. Python의 모든 클래스는 object 클래스를 상속함 => "모든 것은 객체이다."
* 6. MyClass.mro() => 상속 관계를 보여줌
"""
# 파이썬에서 모든 것은 객체이다!!


class Robot(object):  # object는 생략된 것!

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
    def are_you_robot():
        print(f"{Robot.population} num!")
        print("yes!!")

    # str메서드 커스터마이징(=overriding)
    def __str__(self):
        return f"{self.name} robot!!"

    # 실행가능한 객체로 설정
    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


# Robot 클래스를 상속받는 새로운 클래스
# : 자식 클래스(Siri Class)에서 별도의 메서드나 속성을 추가할 수 있음!
class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b


siri = Siri("iphone8")

# 상속관계를 보여주는 메서드 : .mro()
print(Siri.mro())
"""
[<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
"""

print(Robot.mro())
"""
[<class '__main__.Robot'>, <class 'object'>]
"""

# object란 무엇인가?
print(object)
"""
<class 'object'>
"""

print(dir(object))  # object의 속성값 출력
"""
['__class__', '__delattr__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__']
"""

print(object.__name__)
"""
object
"""

print(int.mro())
"""
[<class 'int'>, <class 'object'>]
"""

print(int.__init__(8.9))
print(int(8.9))


# 다중 상속
class A:
    pass


class B:
    pass


class C:
    pass


# 일반적인 다중 상속은 anti-pattern을 유발함!
# mixin 클래스를 이용한 다중 상속이 권장됨!(부품화)
class D(A, B, C):
    pass


print(D.mro())
"""
[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>,
<class '__main__.C'>, <class 'object'>]
"""
