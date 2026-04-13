class Employes:
    language = "paython"
    salary = "1200 USD"

    def __init__(self,name,salary,):
        self.name = name
        self.salary = salary
        print("hello i have done this code to learn")

    def greetings(self):
        print("good moring to everyone")

    def getInfo(self):
        print(f"{self.language} and  {self.salary}")


talha = Employes("talha","1300 USD")
talha.greetings()
talha.getInfo()