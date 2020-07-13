def foo():
    # 1 -- We Do not Define global variable outside So There is no x variable
    # 4 -- This x variable is local and the scope of this x is only inside foo()
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)  # 5 -- x = 20 which is a local variable
    print("Calling bar now")
    bar()  # 6 -- Creating a global x variable which is not associated with local x variable
    # which is inside foo()
    print("After calling bar: ", x)  # 7 -- x = 20 because inside the foo function local x variable


foo()
# 2 -- But Be Define x in bar() which is a global variable
# 3 -- x inside foo() and bar() are Different variable containing Different space in memory.
print("x in main: ", x)  # 8 -- x = 25 because global x variable is created inside bar()
# local variable of foo has no scope outside


# Second Example

a = 5


def fooo():
    # If same Name of variable i.e. global and local
    a = 10
    print("local a:", a)  # if local variable is present first priority is local variable
    # If there is no local variable then use global variable
    # If we want the modify the global variable inside the function so no creation of local variable
    # Then use global keyword


fooo()
print("global a:", a)  # Always take global variable value because in global space there is no scope of
# local variable


# Third Example

# Non local variable is use in nested function
def outer():
    b = "local"

    def inner():
        nonlocal b
        b = "nonlocal"
        print("inner:", b)

    inner()
    print("outer:", b)


outer()