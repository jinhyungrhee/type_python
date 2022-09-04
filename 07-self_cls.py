"""
[self의 이해]
* self는 인스턴스 객체임
* 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같음!
* 즉, self는 인스턴스 그 자체임!
"""


class SelfTest:

    # 클래스 변수
    name = "hinodi5"

    # 생성자
    def __init__(self, x):
        self.x = x  # 인스턴스 변수

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls : {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self : {self}")
        print("class안의 self 주소 : ", id(self))
        print("func2")


test_obj = SelfTest(17)
test_obj.func2()
SelfTest.func1()

print("인스턴스의 주소 : ", id(test_obj))

"""
self : <__main__.SelfTest object at 0x00000225B03AA7F0> # 메모리 위치
class안의 self 주소 :  2360893679600 # 메모리 주소
func2
cls : <class '__main__.SelfTest'>
func1
인스턴스의 주소 :  2360893679600 # 메모리 주소
"""

# func1()는 클래스 메서드임에도 불구하고 Python 내부적으로 '동적'으로 계산이 되어서
# 인스턴스를 통해서 클래스 네임스페이스에 접근해서 클래스 메서드를 호출한 것임!
test_obj.func1()
"""
cls : <class '__main__.SelfTest'>
func1
"""

# Q. 그러면 인스턴스로 클래스 네임스페이스에 접근하여 클래스 네임을 가져올 수 있을까? => 가능
print(test_obj.name)
"""
hinodi5
"""

# Q. 반대로, 클래스에서 인스턴스 네임스페이스에 접근하여 인스턴스 메서드를 실행시킬 수 있을까? => 그냥하면 에러!
SelfTest.func2()
"""
TypeError: func2() missing 1 required positional argument: 'self'
"""

# Q. 클래스에서 인스턴스 네임스페이스에 접근하여 인스턴스 변수를 가져올 수 있을까? => 에러!
print(SelfTest.x)
"""
AttributeError: type object 'SelfTest' has no attribute 'x'
"""
