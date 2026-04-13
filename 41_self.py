class Jober:
    
    language = "poushto"  # these are the class atrributes which are defined in a class 
    salary = "1200 USD"

    def getInfo(self):
        
             print(f"this is the salary  {self.salary} and this is the language {self.language}")
      
    @staticmethod
    # marked as a function jo ka hamari pass self nahi lega and is ma object ki koye be property nahi chahiye
    def greeting():
            print("good morning")

HR  =  Jober()
# Jober.greeting()
HR.greeting()
HR.getInfo()
