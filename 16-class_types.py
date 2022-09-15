"""
* Class Types
* 클래스에 대해 type hint 적용하기
"""

# 정상적인 클래스 사용
class Hello:
    def world(self) -> int:
        return 7


# 이상한 클래스 사용
class World:
    pass


# 클래스에 대한 instance를 typing할 때 '콜론(:)+클래스명'을 써주면 됨!


def foo(ins: Hello) -> int:
    return ins.world()


hello: Hello = Hello()
world: World = World()

print(foo(hello))
"""
$ mypy 16-class_types.py && python 16-class_types.py
Success: no issues found in 1 source file
7
"""
print(foo(world))
"""
$ mypy 16-class_types.py && python 16-class_types.py
16-class_types.py:33: error: Argument 1 to "foo" has incompatible type "World"; expected "Hello"
Found 1 error in 1 file (checked 1 source file)
"""
