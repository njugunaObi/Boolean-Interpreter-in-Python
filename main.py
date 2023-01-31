# I will be attempting problem 4: Creating a boolean logic interpreter

# 1: Creating an example of a simple boolean logic interpreter

A = 5
E = A < 10
print(E)
print(type(A < 10))


B = A > 10
print(B)
print(type(B))



# 2: Using and,or and not within the interpreter
x = 5
y = 10

# Using "and" operator
result1 = (x > 0) and (y > 0)
print(result1)

# Using "or" operator
result2 = (x > 0) or (y > 0)
print(result2)

# Using "not" operator
result3 = not (x > 0)
print(result3)
