
#1 normal function (basic)
print("======= Basic type =======")
# function definition
def greetings(name, msg):
    print(msg,name,"!!")

# calling
greetings("Suraj","Good Morning")
#----------------------------------------------------

print("\n======= default arguments =======")
#2 with default arguments
def greeting2(name, msg="good morning"):
    print(msg,name,"!!")

greeting2("Suraj","Get up")
#----------------------------------------------------

print("\n======= keyword arguments =======")
#3 keyword argument
def greeting3(name, msg):
    print(msg,name,"!!")

# see how we are making the call
greeting3(msg="Get up",name="Suraj")

# greeting3(msg="Get up",Suraj")      # error because positional argument cannot follow keyword argument
greeting3("Suraj",msg="Get up")     # but a keyword argument can follow a positional argument
# greeting3("Get up", name="Suraj")       #invalid because two values passed to name itself
#----------------------------------------------------

print("\n======= arbitrary arguments =======")
#4 arbitrary arguments
def greeting4(msg, *names):
    for name in names:
        print(msg, name, "!!")

greeting4("Wish you a very good morning","Fury","Michael","Suraj","Tarun","Aman","Ajay")