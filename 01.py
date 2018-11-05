"""
定义一个学生类，用来形容学生
"""

#定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    #此处pass必须有
    pass

#定义一个对象
mingyue = Student()

#定义一个类，用来描述Python的学生
class PythonStudent():
    #可以用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    #1.def doHomework的缩进层级
    #2.系统默认有一个self参数
    def doHomework(self):
        print("我在做作业")

        #推荐在函数的末尾使用return语句
        return None

#实体化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)

#注意成员函数的调用没有传入参数
yueyue.doHomework()

