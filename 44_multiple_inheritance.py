
class Employee:
    company = "Encova solutions"
    langauge="paushto"
    salary = "1200 USD"
    userName = "talha ahmad awan"

    def show(self):
        print(f"the name of the employee is {self.userName} and the company is {self.company}")

class Coder:
    language = "python"
    def printLanguages(self):
        print(f"out of all the language here is your language {Employee.langauge}")


class Programmer(Employee, Coder):
    #  company = "Encova sector"
     def showCompany(self):
        print(f"the name of the company is {self.company} and the language is {Coder.language}")


a = Employee()
b = Programmer()


# print(a.company,b.company,a.langauge,b.langauge,b.userName,c.language)
b.show()
b.printLanguages()
b.showCompany()






