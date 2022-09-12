"""
* mypy와 pyright를 사용하여 runtime에서 type을 검사하기
* mypy : https://mypy.readthedocs.io/en/stable/getting_started.html
  - mypy로는 결과를 출력할 수 없기 때문에 mypy로 type checking을 한 뒤, python으로 다시 출력해야 함!
  - 한 줄로 처리하려면 mypy 15-mypy_pyright.py && ptyhon 15-mypy_pyright.py 로 명령해야 함!
* pyright : https://github.com/microsoft/pyright
  - mypy와 사용방법은 동일
  - 조금 더 안정적이고 빠름
  - npm으로 다운받음
  - 한 줄로 처리하려면 pyright 15-mypy_pyright.py && python 15-mypy_pyright.py로 명령해야 함!
* 하지만 mypy, pyright 둘다 python에서 공식적으로 지원하는 type checking 방법은 아님 
* -> 기능적으로 unit test 별로 pyright를 사용하는 것이 좋음
* -> '생산성'과 '경고성'을 동시에 챙길 수 있음!
"""
from typing import List, Tuple, Dict

# int_var: str = 88  # 기존에서는 type check에 통과하지만 mypy에서는 통과하지 못함
"""
* mypy
$ mypy 15-mypy_pyright.py 
15-mypy_pyright.py:8: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)

* pyright
$ pyright 15-mypy_pyright.py 
No configuration file found.
No pyproject.toml file found.
stubPath C:\type_python\typings is not a valid directory.
Assuming Python platform Windows
Searching for source files
Found 1 source file
pyright 1.1.270
C:\type_python\15-mypy_pyright.py
  C:\type_python\15-mypy_pyright.py:10:16 - error: Expression of type "Literal[88]" cannot be assigned to declared type "str"
    "Literal[88]" is incompatible with "str" (reportGeneralTypeIssues)
1 error, 0 warnings, 0 informations
Completed in 0.942sec
"""
int_var: int = 88
"""
* mypy
$ mypy 15-mypy_pyright.py 
Success: no issues found in 1 source file

* pyright
$ pyright 15-mypy_pyright.py
No configuration file found.
No pyproject.toml file found.
stubPath C:\type_python\typings is not a valid directory.
Assuming Python platform Windows
Searching for source files
Found 1 source file
pyright 1.1.270
0 errors, 0 warnings, 0 informations
Completed in 0.944sec
"""
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

list_var: List[int] = [1, 2, 3]

list_var2: List[str] = ["1", "2", "3"]

tuple_var: Tuple[int, ...] = (1, 2, 3)

dict_var: Dict[str, int] = {"hello": 47}

"""
print(isinstance(88, int))  # True
print(isinstance(88.9, float))  # True
print(isinstance(88, bool))  # False
"""


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error: {typer}")


def cal_add(x: int, y: int) -> int:  # -> 뒤에는 return type 명시
    # type check 메서드 활용
    type_check(x, int)
    type_check(y, int)
    return x + y


print(cal_add(1, 3))  # 4

# print(cal_add("1, ", "3, dijkstra"))  # 1, 3, dijkstra

# print(cal_add([1, 3], [4, 5]))  # [1, 3, 4, 5]

print(int_var)
