class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'学员信息: 姓名 {self.name}, 性别 {self.gender}, 手机号 {self.tel}'


if __name__ == '__main__':
    # 测试信息
    s = Student('Lucy', '女', 123456)
    print(s)
