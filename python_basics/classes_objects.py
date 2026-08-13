##                          Classes & Objects                         ##

class Turbine:
    category = "Turbine"
    def __init__(self,name,rated_power,actual_power):
        if rated_power <= 0:
            raise ValueError("Rated power can not be negative")
        self.name = name
        self.rated_power = rated_power
        self.actual_power = actual_power
    # def capacity_factor(self):
    #     return self.actual_power/self.rated_power
    def update_power(self,new_power):
        if new_power < 0:
            raise ValueError("Power can not be negative")
        
        self.actual_power = new_power
        return self.actual_power
    def status(self):
        if self.actual_power == 0:
            return "Stopped"
        elif self.actual_power < self.rated_power:
            return "Running"
        elif self.actual_power == self.rated_power:
            return "At rated power"
        else:
            return "Above rated power"
        
    def capacity_percentage(self):
        return (self.actual_power/self.rated_power)*100

    def has_higher_power_than(self,other):
        if self.actual_power > other.actual_power:
            return True
        else:
            return False
    def has_higher_capacity_percentage_than(self,other):
        return self.capacity_percentage() > other.capacity_percentage()

    def summary(self):
        return(f"Turbine {self.name} | Rated: {self.rated_power} | Actual: {self.actual_power} | Status: {self.status()}")
t1 = Turbine("T1", 3000, 1500)
t2 = Turbine("T2", 5000, 2000)

print(t1.has_higher_power_than(t2))
print(t2.has_higher_power_than(t1))
print()
print(t1.has_higher_capacity_percentage_than(t2))
print(t2.has_higher_capacity_percentage_than(t1))
print()
print(t1.category)
print(t2.category)
print(Turbine.category)