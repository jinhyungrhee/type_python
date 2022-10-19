# final type은 일종의 '상수'임
# Python에서는 '상수'의 개녀미 없어서 암묵적으로 변수를 대문자로 써서 상수처럼 사용 (ex. RATE = 300)
# final type으로 상수임을 명시하면 이후에 값 재할당이 불가능해짐!
from typing_extensions import Final

RATE: Final = 300

RATE = 500
"""
C:\type_python\19-final_types.py
  C:\type_python\19-final_types.py:8:1 - error: "RATE" is declared as Final and cannot be reassigned
1 error, 0 warnings, 0 informations
Completed in 0.843sec
"""
