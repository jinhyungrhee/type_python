# 이러한 유닛 테스트에서 mypy나 pyright 사용하는 것이 권장됨!
# -> 거대한 웹 서비스를 만들 때 하나하나 pyright로 검사해가면서 개발하는 것보다
#    필요한 함수가 있을 때, 그것이 중요한 함수면 test코드를 작성한 뒤 pyright로
#    검사하면서 테스트를 진행하는 것이 바람직!
def cal_add(x: int, y: int) -> int:
    # code
    return x + y


print(cal_add(1, 3))

"""
$ pyright test.py && python test.py
No configuration file found.
No pyproject.toml file found.
stubPath C:\type_python\typings is not a valid directory.
Assuming Python platform Windows
Searching for source files
Found 1 source file
pyright 1.1.270
0 errors, 0 warnings, 0 informations 
Completed in 0.841sec
4
"""
