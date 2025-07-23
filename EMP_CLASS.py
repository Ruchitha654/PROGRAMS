class emp:
    tax=10
    company="COGNIZANT"  
    profit=100000
    def __init__ (self,name,age,salary,per):
        self.name=name
        self.age=age
        self.salary=salary
        self.per=per
    def cal_tax(self):
        return ((emp.tax/100)*self.salary)
    def cal_share(self):
        return ((self.per/100)*emp.profit)
    def display(self):
        print("Company:{}".format(emp.company))
        print("Name:{}".format(self.name))
        print("Age:{}".format(self.age))
        print("Salary:{}".format(self.salary))
        print("tax:{}".format(self.cal_tax()))
        print("Share:{}".format(self.cal_share()))
s1=emp("Ruchi",21,80000,5)
s1.display()
print("------------------------------")
s2=emp("Ruchitha",30,150000,6)
s2.display()