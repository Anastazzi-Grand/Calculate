from decimal import Decimal, InvalidOperation


def priority(i):
    if i == '*':
        return 2
    if i == '/':
        return 2
    if i == '+':
        return 1
    if i == '-':
        return 1


def postfix(exp):
    queue = []
    op_stack = []
    for token in exp:
        if token not in ('-', '+', '*', '/'):
            queue.append(token)
        elif token in ('-', '+', '*', '/'):
            while op_stack and (priority(op_stack[-1]) >= priority(token)):
                queue.append(op_stack.pop())
            op_stack.append(token)
    while op_stack:
        queue.append(op_stack.pop())
    return queue


def calc(postfx):
    stack = []
    for value in postfx:
        if value in ['-', '+', '*', '/']:
            o1 = stack.pop()
            o2 = stack.pop()
            if value == '-':
                stack.append(o2 - o1)
            if value == '+':
                stack.append(o2 + o1)
            if value == '*':
                stack.append(o2 * o1)
            if value == '/':
                if o1 == 0:
                    print('Division by zero')
                stack.append(o2 / o1)
        else:
            stack.append(Decimal(value))
    return stack.pop()


def calculate():
    formula = input('> ')
    tok_formula = formula.split(' ')
    final_exp = postfix(tok_formula)
    print(calc(final_exp))


while True:
    calculate()
