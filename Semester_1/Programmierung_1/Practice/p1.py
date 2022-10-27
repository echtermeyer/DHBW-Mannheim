tokens = "10 20 + 10 *".split(" ")

stack = []

for val in tokens:
    if val.isdigit():
        stack.append(int(val))

    elif val == "+":
        stack.append(stack.pop() + stack.pop())
    elif val == "-":
        stack.append(stack.pop() - stack.pop())
    elif val == "*":
        stack.append(stack.pop() * stack.pop())
    elif val == "/":
        stack.append(stack.pop() / stack.pop())

print(*stack)
