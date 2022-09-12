# Python에서의 Type Hints
int_var: int = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

int_var: str = 88
"""
* no error checked
* : type hint이기 때문에 따로 type check는 하지 않음!
"""
from typing import List, Tuple, Dict

list_var: List[int] = [1, 2, 3]

list_var2: List[str] = ["1", "2", "3"]

tuple_var: Tuple[int, ...] = (1, 2, 3)

dict_var: Dict[str, int] = {"hello": 47}


# 내 의도는 x, y가 int로 입력되기만을 바랬지만,
# 다른 사람들은 int 이외에도 다른 type으로 값을 넣을 수 있음!
# => 이 경우, 의도한 함수의 기능을 잃게되는 것!
# => 생산성이 좋은 동적 언어를 사용해서 typing 역시 쉽게 사용을 했지만,
#    다른 개발자와 협엽 시 유지보수를 할 때 큰 어려움이 발생할 수 있음!
# => 이를 방지하기 위해 type hint 사용!

# 하지만 이것만으로는 type checking을 할 수 없음!
# validation method 사용 : isinstance(obj, class) 활용

"""
print(isinstance(88, int))  # True
print(isinstance(88.9, float))  # True
print(isinstance(88, bool))  # False
"""

# 일일이 type_check하는 것은  생산성이 떨어질 수 있지만
# 중요한 함수에서는 사용하는 것이 좋음!
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
