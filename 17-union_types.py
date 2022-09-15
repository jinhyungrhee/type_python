"""
* Union Types
* 동일한 변수에 대해 여러가지 type을 적용하고 싶은 경우 사용
* 예시 - xxx: Union[int, str] => xxx변수에는 int값이 할당될 수도 있고, string값이 할당될 수도 있음!
"""
from typing import Union

# 동일한 변수에 대해 Type을 변경할 경우 mypy는 에러를 발생시킴
# xxx: int = 3
# xxx = "17"
"""
$ mypy 17-union_types.py && python 17-union_types.py 
17-union_types.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
"""

# 동일한 변수에 대해 여러가지 type을 동시에 적용시키는 경우 Union typing 사용
xxx: Union[int, str] = 3
xxx = "17"  # OK
# xxx = 3 # OK
# xxx = 123.45 # TYPE ERROR
"""
$ mypy 17-union_types.py && python 17-union_types.py 
Success: no issues found in 1 source file
"""


# Union typing을 함수에 적용한 경우(return값 X)
# def foo(x: Union[int, str]) -> None:
#     print(x)


# Union typing을 함수에 적용한 경우(return값 O)
def foo(x: Union[int, str]) -> Union[int, str]:
    return x


# foo(xxx)
print(foo(xxx))
"""
$ mypy 17-union_types.py && python 17-union_types.py 
Success: no issues found in 1 source file
17
"""
