"""
* 객체 내에 있는 변수들은 __dict__를 통해서 관리가 됨
* __slots__를 통해서 변수 관리
* 파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한함
* __dict__를 통해 관리되는 객체의 성능을 최적화 -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소
"""

# ============================ __dict__ 사용 =====================================


class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("hinodi5", 12)

print(wos.__dict__)
"""
{'name': 'hinodi5', 'age': 12}
"""

# 객체에 attribute 추가 (dynamic하게 추가 가능)
wos.__dict__["hello"] = "world"

print(wos.__dict__)
"""
{'name': 'hinodi5', 'age': 12, 'hello': 'world'}
"""


# ========================= __slots__ 사용 ==============================
# __dict__처럼 dynamic하게 추가되는 것을 막고 필요한 속성(attribute)들만
# 미리 지정(제한)해놓으면 성능이 더 좋아질 것! => __slots__  사용 이유!
# 즉, 속성(attribute)들을 미리 선언해놓는 것!


class WithSlotClass:
    # __dict__ 대신 __slots__로 속성 관리
    __slots__ = ["name", "age"]  # dict 자료형이 아닌 리스트 자료형

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("hinodi5", 12)

# print(ws.__dict__)
"""
AttributeError: 'WithSlotClass' object has no attribute '__dict__'
"""

print(ws.__slots__)
"""
['name', 'age']
"""

# 성능 테스트
import timeit

# 메모리 사용량 비교


def repeat(obj):
    def inner():
        obj.name = "hinodi5"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=99999)
no_slot_time = timeit.repeat(repeat(wos), number=99999)

print("use slot : ", min(use_slot_time))
"""
use slot :  0.05757110000000004
"""
print("no slot  : ", min(no_slot_time))
"""
no slot  :  0.07119449999999994
"""
