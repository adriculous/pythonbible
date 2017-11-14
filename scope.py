# variable scopes (global (scope outside functions) and local (scope inside functions))

a = 250 # this is a global variable scope

def f1(): # adding parameters inside the parentheses are optional
    global a # global keyword, redefines default global scope
    a = 100
    print(a)

def f2():
    a = 50 # this is a local variable scope, will be different from global variable
    print(a)

f1()
f2()
print(a)

# What I learned about variable scopes
# 1) Two types of scopes - global & local
# 2) Python functions create local scopes
# 3) You can't override a global scope from a local scope (inside a function) unless if you use the "global" keyword
# 4) Lists and dictionaries will also not override a global scope, but you can change a value within a list or dictionary from within a function.
