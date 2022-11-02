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


def to_postfix(exp):
    queue = []
    operand_stack = []
    for token in exp:
        if token not in ('-', '+', '*', '/'):
            queue.append(token)
        elif token in ('-', '+', '*', '/'):
            while operand_stack and (priority(operand_stack[-1]) >= priority(token)):
                queue.append(operand_stack.pop())
            operand_stack.append(token)
    while operand_stack:
        queue.append(operand_stack.pop())
    return queue


def calc(postfix):
    stack = []
    for value in postfix:
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
    formula = input(' ')
    token_formula = formula.split(' ')
    final_exp = to_postfix(token_formula)
    print(calc(final_exp))


while True:
    calculate()
