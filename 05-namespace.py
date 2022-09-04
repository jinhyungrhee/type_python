"""
* namespace : 개체를 구분할 수 있는 범위
* __dict__ : 네임스페이스를 확인할 수 있음(딕셔너리 형태로 반환)
* dir() : 네임스페이스의 key 값을 확인할 수 있음
* __doc__ : class의 주석을 확인함
* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있음
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
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
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
        print(f"we have {cls.population} robots.")


siri = Robot("siri", 21039788127)
jarvis = Robot("jarvis", 2311213123)
bixby = Robot("bixby", 124312423)


# ========================== __dict__ ==================================
# : 클래스 네임스페이스 출력
# : 물리적인 단계에서 보여줌
print(Robot.__dict__)
"""
{'__module__': '__main__',
'population': 3,
'__init__': <function Robot.__init__ at 0x000002292B28F280>,
'say_hi': <function Robot.say_hi at 0x000002292B28F310>,
'cal_add': <function Robot.cal_add at 0x000002292B28F3A0>,
'die': <function Robot.die at 0x000002292B28F430>,
'how_many': <classmethod object at 0x000002292B249BE0>,
'__dict__': <attribute '__dict__' of 'Robot' objects>,
'__weakref__': <attribute '__weakref__' of 'Robot' objects>,
'__doc__': None}
"""
# Q. say_hi, call_add, die 같은 인스턴스 메서드들이 왜 클래스 네임스페이스에 들어와있는가?


# 인스턴스 네임스페이스 출력
print(siri.__dict__)  # {'name': 'siri', 'code': 21039788127}
print(jarvis.__dict__)  # {'name': 'jarvis', 'code': 2311213123}
print(bixby.__dict__)  # {'name': 'bixby', 'code': 124312423}
# => 인스턴스 공간(네임스페이스)임에도 인스턴스 메서드는 들어가있지 않음!

# A. 일반적으로 함수에 새로운 함수를 할당하는 경우는 많이 없으므로,
#    메모리 효율을 위해서 클래스 네임스페이스에 인스턴스 메서드들이 저장되도록 설계됨

print(siri.name)
print(bixby.name)
# Python 내부적으로 인스턴스 네임스페이스에 없으면 클래스 네임스페이스에서 찾도록 설계됨**
siri.cal_add(2, 3)
# 동일한 원리로 인스턴스를 사용해 클래스 변수와 클래스 메서드에 접근할 수 있음**
print(siri.population)
siri.how_many()

# 그 반대의 경우(클래스 네임스페이스 -> 인스턴스 메서드 호출) 그냥은 불가능!
# Robot.say_hi()
"""
TypeError: say_hi() missing 1 required positional argument: 'self'
"""

# 이를 가능하게 하기 위해서는 인스턴스 객체를 매개변수로 넣어주면 됨!
Robot.say_hi(siri)  # 서로 동일
siri.say_hi()  # 서로 동일


# ================ __dir__ =====================================
# : 네임스페이스를 조금 더 사용자화해서 제공하는 메서드(built-in)
# : 해당 인스턴스/클래스에서 접근 가능한 키 값들을 모두 출력함!

print(dir(siri))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__','__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__','__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', 'cal_add', 'code', 'die',
 'how_many', 'name', 'population', 'say_hi']
"""

print(dir(Robot))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 'cal_add', 'die', 'how_many', 'population', 'say_hi']
"""

# ======================== __doc__ ======================================
# : 클래스 내부 코드를 전체 읽지 않아도 클래스 관련 주석만 읽고서 바로 클래스를 사용할 수 있도록 주석 작성함
# : __doc__은 이러한 클래스 내부 주석을 확인할 수 있도록 도와주는 메서드
print(Robot.__doc__)
"""
    [Robot Class]
    Author : 홍길동
    Role : ?????
"""


# ==================== __clas__ ===========================================
# : 인스턴스가 어떤 클래스로 만들어졌는지 확인하는 메서드
print(siri.__class__)
"""
<class '__main__.Robot'>
"""
