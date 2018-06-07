# FUNCTIONS ARE BLOCKS OF CODE THAT RUNS WHEN IT IS CALLED
# IT MAY RECEIVE PARAMETERS (DATA)
# IT MAY RETURN DATA


# TO CREATE A FUNCTION IN PYTHON WE USE THE WORD DEF
def new_function():
    print("This is my function")


# CALLING THE FUNCTION
new_function()


# PASSING PARAMETER TO THE FUNCTION
def say_my_name(name):
    print("My name is " + name)


# CALLING THE FUNCTION
say_my_name("John")


# USE DEFAULT PARAMETER IN FUNCTIONS
def default_function(parameter="default"):
    print("My default value is " + parameter)


# CALLING THE FUNCTION TO PRINT DEFAULT PARAMETER
default_function()


# CALLING THE FUNCTION AND OVERWRITE DEFAULT PARAMETER
default_function("not default")


# FUNCTION THAT RETURNS A VALUE
def sum_values(a, b):
    return a + b


# CALLING THE FUNCTION AND PRINTING THE RETURNED VALUE
print(sum_values(1, 1))


# LAMBDA FUNCTION : USE THE LAMBDA KEYWORD
# ALSO CALLED AS ANONYMOUS FUNCTION
# SAME SUM FUNCTION IN LAMBDA
lambdaFunction = lambda a, b: a + b


# CALLING LAMBDA FUNCTION AND PRINTING THE VALUE
print(lambdaFunction(1, 1))


# GENERATING RUN-TIME FUNCTION WITH LAMBDA
def lambda_function(x):
    return lambda a: a * x


# RUN-TIME ASSIGN TO A VARIABLE AND PRINTING RETURNED VALUES
fiveTimes = lambda_function(5)
print(fiveTimes(2))
tenTimes = lambda_function(10)
print(tenTimes(2))