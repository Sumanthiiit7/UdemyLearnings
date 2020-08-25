print('hello world')

def new_function():
    print("Trying to print the new line")
    print("still inside")

print("first out")
new_function()
print("outside")

def default_argument(arg1 = "Not Provided", arg2 = "Not Provided"): #default arguements -> If we dont send any arguement then the arguement will be dafaulted
    print(arg1)
    print(arg2)

default_argument("sumanth","testing")
default_argument(arg2="sumanth", arg1=20) #passing it with arguement name