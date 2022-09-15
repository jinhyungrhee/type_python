"""
* Optional Types
* 있을 수도 있고, 없을 수도 있는 Type 지정
* Optional Types는 Union Types로 대체될 수 있음!(= 유사한 기능)
"""
from typing import Union, Optional


# Union Types를 사용한 경우
xxx: Union[str, None] = "hinodi5"

xxx = None


# Optional Types를 사용한 경우
yyy: Optional[str] = "hinoi5"

yyy = None


# Optional Types가 필요한 이유 : '있을 수도 있고, 없을 수도 있는 경우가 많기 때문!'
def foo(name: str) -> Optional[str]:
    if name == "hinodi5":
        return None
    else:
        return name


result: Optional[str] = foo("hinodi5")
print(result)
"""
$ mypy 18-optional_types.py && python 18-optional_types.py 
Success: no issues found in 1 source file
None
"""
