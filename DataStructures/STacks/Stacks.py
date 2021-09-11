# Lifo principles
# Basic operations of stack
# push,pop, is empty, is full, peek

# STack implementation in Python

def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    return stack.append(item)


def pop_item(stack, item):
    if (check_empty(stack)):
        return "Stack is Empty"
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print(str(stack))

# Stack Applications
# - Reverse a word(pop items one by one)
# - Compilers
# - Browsers(back button)
