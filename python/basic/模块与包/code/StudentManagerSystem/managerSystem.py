from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据的列表
        self.student_list = []

    def run(self):
        """程序入口方法, 启动程序后执行的方法"""
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input('请输入你需要的功能序号: '))

            if menu_num == 1:
                # 添加学员信息
                self.add_student()
            elif menu_num == 2:
                # 删除学员信息
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_studnet()
            elif menu_num == 7:
                # 退出系统
                break

    @staticmethod
    def show_menu():
        """显示功能菜单"""
        print('请选择如下功能: ')
        print('1. 添加学员信息')
        print('2. 删除学员信息')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 保存学员信息')
        print('7. 退出系统')

    def add_student(self):
        """添加学员信息"""
        name = input('请输入学员的姓名: ')
        gender = input('请输入学员的性别: ')
        tel = input('请输入学员的手机号: ')

        student = Student(name, gender, tel)

        self.student_list.append(student)

    def del_student(self):
        """删除学员信息"""
        del_name = input('请输入要删除的学员姓名: ')

        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')

    def modify_student(self):
        """修改学员信息"""
        modify_name = input('请输入要修改的学员姓名: ')

        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名: ')
                i.gender = input('请输入学员性别: ')
                i.tel = input('请输入学员手机号: ')
                print(f'修改学员信息成功, 姓名 {i.name}, 性别 {i.gender}, 手机号 {i.tel}')
                break
        else:
            print('查无此人')

    def search_student(self):
        """查询学员信息"""
        search_name = input('请输入要查询的学员姓名: ')

        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名 {i.name}, 性别 {i.gender}, 手机号 {i.tel}')
                break
        else:
            print('查无此人')

    def show_student(self):
        """显示所有学员信息"""
        print('姓名\t性别\t手机号')

        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_studnet(self):
        """保存学员信息"""
        f = open('student.data', 'w')

        # 注意: 文件写入的数据不能是学员对象的内存地址,
        # 需要把学员数据转换成字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]

        # 注意: 文件内部数据要求为字符串类型,
        # 需要先将数据类型转换为字符串才能向文件写入数据
        f.write(str(new_list))

        f.close()

    def load_student(self):
        """加载学员信息"""
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()

            # 文件中读取的数据都是字符串
            # 故需要转换数据类型为对象后存储到学员列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()


if __name__ == '__main__':
    # 测试信息
    mgr = StudentManager()
    mgr.run()
