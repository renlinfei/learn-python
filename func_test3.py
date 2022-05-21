# a*x + b
# a =1, b = 2
# y = ?
def a_line(a, b):
    def arg_y(x):
        return a * x + b
    return arg_y
line1 = a_line(1, 2)
print(line1(3))
print(line1(4))