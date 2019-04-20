# create a calculator function
# input = "(2+2)*4"
# input is a string
# output shud be integer 16 in this case
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
def applyop(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
def evaluate(tokens):
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i] == ' ':
            i += 1
            continue
        elif tokens[i] == '(':
            ops.append(tokens[i])
        elif tokens[i].isdigit():
            val = 0
            while (i < len(tokens) and tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1
            else:
                i=i-1
            values.append(val)

        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyop(val1, val2, op))
            ops.pop()
        else:
            while (len(ops) != 0 and
                   precedence(ops[-1]) >= precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyop(val1, val2, op))
            ops.append(tokens[i])
        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyop(val1, val2, op))
    return values[-1]
s ='(2+3*14)+126/2'
print(evaluate(s))
