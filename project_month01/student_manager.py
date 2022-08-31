"""
    步骤一：
        数据模型类：StudentModel
		    数据：编号 id,姓名 name,年龄 age,成绩 score
	    逻辑控制类：StudentManagerController
		    数据：学生列表 __stu_list
		    行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，
"""
class StudentModel:
    """
        学生数据模型类
    """
    def __init__(self, name="", age=0, score=0,id=0):
        self.name =name
        self.age = age
        self.score=score
        self.id = id
class StudentManagerController:
    """
        学生管理控制器：主要负责业务逻辑处理
    """
    init_id = 1000
    @classmethod
    def __generte_id(cls,stu):
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu):
        StudentManagerController.__generte_id(stu)
        self.__stu_list.append(stu)

    def remove_student(self,stu_id):
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False
    def update_student(self,new_stu):
        for item in self.__stu_list:
            if item.id == new_stu.id:
                item.name = new_stu.name
                item.age = new_stu.age
                item.score = new_stu.score
                return True
        return False
    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[c].score:
                    self.__stu_list[i], self.__stu_list[c]=self.__stu_list[c], self.__stu_list[i]
#
# student01 = StudentModel("张三",56,89)
# student02 = StudentModel("李四",16,100)
# student03 = StudentModel("李5",16,1020)
# controller = StudentManagerController()
# controller.add_student(student01)
# controller.add_student(student02)
# controller.add_student(student03)
# # print(controller.update_student(StudentModel("张8",100,89,1003)))
# # print(controller.remove_student(1001))
# controller.order_by_score()
# for i in controller.stu_list:
#     print(i.id,i.name)
