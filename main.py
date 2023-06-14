# third에게 add.py add_func(정수, 정수), 리턴 정수
# third에게 mul.py mul_func(정수, 정수), 리턴 정수
# 나는 sub.py sub_func(정수, 정수), 리턴 정수
# 나는 div.py div_func(정수, 정수), 리턴 정수
from add import add_func
from sub import sub_func
from mul import mul_func
from div import div_func
## 함수



## 변수
num1, num2,res = 100, 200, 0


## 메인
res = add_func(num1, num2)
print(res)

res = sub_func(num1, num2)
print(res)

res = mul_func(num1, num2)
print(res)

res = div_func(num1, num2)
print(res)

print('고생하셨습니다 완성')