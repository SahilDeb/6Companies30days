# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

def evalRPN(tokens) -> int:
    vals = []
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    for ch in tokens:
        if ch in operations:
            sec = vals.pop()
            fir = vals.pop()
            res = operations[ch](fir, sec)
            vals.append(res)
        else:
            vals.append(int(ch))
    return vals.pop()


# test cases
x1 = ["2", "1", "+", "3", "*"]
x2 = ["4", "13", "5", "/", "+"]
x3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(x3))
