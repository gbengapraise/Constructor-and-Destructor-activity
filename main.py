class Employee:
    def __init__(self):

        print("Employee Created")
    
    def __del__(self):
        print("Employee deleted")
    
emp = Employee()
del emp