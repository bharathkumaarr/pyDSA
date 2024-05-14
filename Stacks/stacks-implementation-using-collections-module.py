# implementation of stack using collections module

'''
push ---> append() method of deque class
pop  ---> pop() method of deque class
'''

import collections
stack = collections.deque()

def append_to_stack():
    if len(stack)!=n:
        x=input("enter the element to append/push to stack: ")
        stack.append(x)
    else:
        print("stack full!")

def remove_from_stack():
    if not(not stack):
        stack.pop()
        print("your new stack is: ", stack)
    else:
        print("stack empty")

def peek():
    if not stack:
        print("stack empty")
    else:
        print("top element of your stack is: ", stack[-1])

n=int(input("enter the lenght limit of the stack: "))
while True:
    print('''
enter your choice:
1.Push
2.Pop
3.Peek
4.Display Stack
6.Quit''')
    ch = int(input())
    if ch == 1:
        append_to_stack()
    elif ch == 2:
        remove_from_stack()
    elif ch == 3:
        peek()
    elif ch == 4:
        print("your stack is: ", stack)
    elif ch == 6:
        break
