"""
* Callable Types
* 함수 인자에 대해 type hint 적용하기
* 첫 번째 인자: 입력받는 인자들에 대한 type 명시
* 두 번째 인자: return값에 대한 type 명시
* 예시 - func: Callable[[int, int], int]
"""
from typing import Callable


# 정상적인 함수 테스트
def add(a: int, b: int) -> int:
    return a + b


# 이상한 함수 테스트
def tests():
    pass


# return이 없는 함수의 경우
# def add(a: int, b: int):
#     print(a + b)


# print(add(1, 3)) # 통과
# print(add(1, "3")) # 에러


# 함수 자체를 인자로 받는 경우
def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo(add))
"""
$ mypy 15-callable_types.py && python 15-callable_types.py
Success: no issues found in 1 source file
5
"""
print(foo(tests))
"""
$ mypy 15-callable_types.py && python 15-callable_types.py
15-callable_types.py:36: error: Argument 1 to "foo" has incompatible type "Callable[[], Any]"; expected "Callable[[int, int], int]"
Found 1 error in 1 file (checked 1 source file)
"""
