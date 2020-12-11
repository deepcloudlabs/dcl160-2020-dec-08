def is_odd(n):
    return n%2 == 1

def is_even(n):
    """
       return true if n is even; false otherwise
    """
    return n%2 == 0

class Employee:
    
    def __init__(self,fullname,salary,department):
        
        self.fullname = fullname
        self.salary = salary
        self.department = department