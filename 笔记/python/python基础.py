# python基础
# 1. 输入与输出
# 输入函数 - 从用户获取数据（返回字符串类型）
name = input("请输入你的姓名：")

# 输出函数 - 打印内容到控制台
print("你好，", name)  # 逗号分隔自动加空格
print(f"希望{name}复习顺利！")  # f-string格式化（推荐）
print("年龄：" + str(20))  # 字符串拼接

# 2. 变量
# 变量命名规则：字母/下划线开头，由字母/数字/下划线组成
age = 18  # 整型变量
height = 1.75  # 浮点型变量
is_student = True  # 布尔型变量
message = "Python很有趣！"  # 字符串变量

# 变量重新赋值
counter = 10
counter = counter + 1  # 变量更新

# 3. 数据类型
# 基本数据类型
num_int = 30        # 整数 int
num_float = 3.14    # 浮点数 float
text = "Hello"      # 字符串 str
is_valid = True     # 布尔值 bool

# 容器类型
my_list = [1, 2, 3, "a", "b"]          # 列表（可变）
my_tuple = (1, "apple", True)           # 元组（不可变）
my_dict = {"name": "Alice", "age": 20}  # 字典（键值对）
my_set = {1, 2, 3, 3, 2}                # 集合（去重）实际存储{1,2,3}

# 4. 运算符
# 算术运算符
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333... (浮点除法)
print(10 // 3)  # 3 (整除)
print(10 % 3)   # 1 (取模)
print(2 ** 4)   # 16 (幂运算)

# 比较运算符
print(5 > 3)    # True
print(5 == 5.0) # True (值相等)
print(5 != "5") # True (类型不同)

# 逻辑运算符
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 5. 类型转换
# 显式类型转换
num_str = "123"
num_int = int(num_str)    # 字符串→整数
num_float = float("3.14") # 字符串→浮点数
str_num = str(456)        # 整数→字符串

# 隐式转换（自动）
result = 5 + 2.5  # int + float → float (7.5)

# 类型检查
print(type("hello"))      # <class 'str'>
print(isinstance(10, int)) # True

# 6. 条件分支流程
score = 85

# 单分支
if score >= 60:
    print("及格！")

# 双分支
if score >= 90:
    print("优秀")
else:
    print("良好" if score >= 70 else "及格")  # 三元表达式

# 多分支
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"等级：{grade}")

# 7. 循环流程
# for循环（遍历序列）
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# range()函数
for i in range(3):        # 0,1,2
    print(f"计数:{i}")

# while循环
count = 3
while count > 0:
    print(f"倒计时：{count}")
    count -= 1  # 等同于 count = count - 1

# 循环控制
for num in range(10):
    if num == 3:
        continue  # 跳过当前迭代
    if num == 7:
        break     # 终止循环
    print(num)

# 8. 函数
def calculate_area(length, width=1):
    """计算矩形面积，默认宽度为1（正方形）"""
    area = length * width
    return area

# 函数调用
print("\n函数演示:")
print("矩形面积:", calculate_area(5, 3))
print("正方形面积:", calculate_area(4))  # 使用默认参数

# 递归函数示例
def factorial(n):
    """计算阶乘的递归函数"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("5的阶乘:", factorial(5))
# 9. 正则表达式
import re

# 基本匹配
text = "联系电话: 138-1234-5678, 备用: 150-9876-5432"
pattern = r"\d{3}-\d{4}-\d{4}"  # 匹配手机号模式

print("\n正则表达式演示:")
# 查找所有匹配
phones = re.findall(pattern, text)
print("找到的电话号码:", phones)

# 替换操作
masked_text = re.sub(r"\d{4}", "****", text)  # 隐藏后四位
print("脱敏后的文本:", masked_text)

# 验证邮箱格式
def is_valid_email(email):
    """验证邮箱格式是否有效"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

print("邮箱验证:")
print("test@example.com:", is_valid_email("test@example.com"))
print("invalid_email:", is_valid_email("invalid_email"))

# 教学结束
print("\n恭喜完成Python基础学习！")

# 深入详细补充：
# 列表
fruits = ["apple", "banana", "cherry", "orange"]

# 列表操作
print("第一个水果:", fruits[0])      # 索引访问
print("最后两个水果:", fruits[-2:])  # 切片操作

# 修改元素
fruits[1] = "blueberry"  # 修改第二个元素
fruits.append("grape")   # 添加元素到末尾
fruits.insert(1, "pear") # 在指定位置插入

# 删除元素
removed = fruits.pop(2)  # 删除并返回第三个元素
fruits.remove("orange")  # 删除指定元素

# 列表方法
print("列表长度:", len(fruits))
print("排序后:", sorted(fruits))  # 返回新排序列表
fruits.sort()            # 原地排序

# 列表遍历
print("\n水果列表:")
for i, fruit in enumerate(fruits):
    print(f"{i+1}. {fruit}")

# 元组
# 创建元组
colors = ("red", "green", "blue")
rgb = (255, 128, 0)  # RGB颜色值

# 元组操作
print("\n基础颜色:", colors[0])
print("RGB值:", rgb)

# 元组解包
r, g, b = rgb
print(f"红色分量: {r}, 绿色分量: {g}, 蓝色分量: {b}")

# 元组不可变性演示
try:
    colors[1] = "yellow"  # 会引发错误
except TypeError as e:
    print("元组不可修改错误:", e)

# 字符串
text = " Python 编程基础 "
print("\n原始字符串:", text)

# 常用字符串方法
print("去除空格:", text.strip())
print("大写转换:", text.upper())
print("替换:", text.replace("编程", "程序设计"))
print("查找'基础':", text.find("基础"))
print("是否以'Py'开头:", text.startswith("Py"))

# 字符串格式化
price = 19.99
quantity = 3
print(f"总价: {price * quantity:.2f}元")  # 保留两位小数

# 字典
student = {
    "name": "张三",
    "age": 20,
    "courses": ["数学", "英语", "编程"],
    "gpa": 3.7
}

# 字典操作
print("\n学生姓名:", student["name"])
print("所有键:", student.keys())
print("所有值:", student.values())

# 安全访问
print("电话:", student.get("phone", "未提供"))  # 避免KeyError

# 添加/修改元素
student["email"] = "zhangsan@example.com"  # 添加新键
student["age"] = 21  # 修改值

# 字典遍历
print("\n学生信息:")
for key, value in student.items():
    print(f"{key}: {value}")