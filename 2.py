class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def create_obj():
    print("Making Objects...")
    obj = Employee()
    print("Function end...")
    return obj

print("calling creates_obj() function...")
obj = create_obj()
print("Program End...")
    