# *args and **kwargs (VERY IMPORTANT FOR INTERVIEWS)

def student_info(**details):
    print(details)
    
def demo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

def total(*arr):
    print(type(arr),arr)
    print(type(type(arr)), str(type(type(arr))).split("'")[1])
    return sum(arr)

student_info(name="Arvind", age=22, branch="CSE")
demo(1,"ab",12,24,52,6,[1,23],d="kdjf",c=12,shift=2,eye="Blue")
print(total(12,13,4,2,13,1,4))
