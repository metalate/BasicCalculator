#calculator project

class Calc(object):
    "calculator"
    # init metodu
    def __init__(self, a, b):
        "initialize values"
        # attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
        
    def multiply(self):
        "mutltiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def subtract(self):
        "subtraction a-b = result -> return result"
        return self.value1 - self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
    
