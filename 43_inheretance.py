langauge = "paushto "
salary = "1200 USD"


class Employee:
    company = "Encova solutions"
    langauge = "paushto "
    salary = "1200 USD"
    userName = "talha ahmad awan"
    def show(self):
        self.language = language
        self.salary = salary
        print(f"the name of the employee is {self.name} and the language is {self.language}")


# class Programmer:
#     company = "The IT solutions"
#     def show(self):
#         print(f"the name of the person is {self.name} and the salary  {self.salary}")  

#     def showLanguage(self):
#         printf("the name is {self.name} and the language he is speaking is {self.language}")   


class Programmer(Employee):
     company = "Encova sector"
    #  def show(self):
    #     print(f"the name of the employee is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

print(a.company,b.company,a.langauge,b.langauge,b.userName)





