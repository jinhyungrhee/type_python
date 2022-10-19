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


# def foo(ins: Hello) -> int:
#     return ins.world()


# hello: Hello = Hello()
# world: World = World()

# 클래스 타입을 ""로 묶어서 사용해도 정상 작동함!
hello: "Hello" = Hello()
world: "World" = World()


def foo(ins: "Hello") -> int:
    return ins.world()


print(foo(hello))
"""
$ mypy 16-class_types.py && python 16-class_types.py
Success: no issues found in 1 source file
7
"""
# print(foo(world))
"""
$ mypy 16-class_types.py && python 16-class_types.py
16-class_types.py:33: error: Argument 1 to "foo" has incompatible type "World"; expected "Hello"
Found 1 error in 1 file (checked 1 source file)
"""

# ** optional과 class를 함께 사용하는 패턴 **
# : 클래스 안에서 자기 자신을 선택하는 경우
# => 클래스 안에서 자기 자신을 typing 하는 경우에는 반드시 ""를 붙이고 Optional을 사용해서 typing을 해야 함!


from typing import Optional


# Optional은 Union["Node", None]과 동일함
# => None이 될 수도 있고, "Node"가 될 수 도 있음!


class Node:
    # def __init__(self, data: int, node: Node):
    # def __init__(self, data: int, node: "Node"):
    def __init__(self, data: int, node: Optional["Node"]):
        self.data = data
        self.node = node


# node = Node(12) # 에러
# 자기 자신의 또 다른 클래스를 담고 있는 형태 **
node2 = Node(12, None)

node1 = Node(27, node2)

node0 = Node(30, node1)
