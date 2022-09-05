"""
[클래스 상속]
* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속됨
* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있음
* 3. 메서드 오버라이딩
* 4. super()
* 5. Python의 모든 클래스는 object 클래스를 상속함 => "모든 것은 객체이다."
* 6. MyClass.mro() => 상속 관계를 보여줌
"""
# init이 부모 클래스에도 있고 자식 클래스에도 있으면 자식 클래스의 것으로 덮어씌워짐
# => 메서드 오버라이딩!


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

    # 생성자 메서드 오버라이딩
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Robot.population += 1 # Robot에 클래스 변수(population) 존재!
        Siri.population += 1  # 둘 다 가능
        # self.population += 1 # 이건 안 됨! (인스턴스 변수에 population이 없기 때문!)

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    # 클래스 메서드나 static method도 정의하여 사용할 수 있음!
    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!")

    # 메서드 오버라이딩
    def say_hi(self):
        print(f"Greetings, my master call me {self.name} by apple.")

    # 클래스 메서드도 오버라이딩 가능
    @classmethod
    def how_many(cls):
        return f"we have {cls.population} robots by apple."


siri = Siri("iphone8", 17)

# 오버라이딩 전 결과
siri.say_hi()
"""
Greetings, my master call me iphone8.
"""

# 오버라이딩 후 결과 => 아예 덮어씌워짐
siri.say_hi()
"""
Greetings, my master call me iphone8 by apple.
"""
print(Siri.how_many())
"""
we have 1 robots by apple.
"""
