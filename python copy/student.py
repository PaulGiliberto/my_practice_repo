class Student:
    def __init__(self,fname,lname,id,energy_level=10):
        self.fname=fname
        self.lname=lname
        self.id=id
        self.energy_level=energy_level
    
    def __str__(self):
        return f"{self.lname}:{self.id}"
    
    def greeting(self):
        return f"Hello, my name is {self.fname} {self.lname}."
    
    def take_exam(self):
        if self.energy_level>1:
            self.energy_level-=1
    
    def get_energy_level(self):
        return self.energy_level