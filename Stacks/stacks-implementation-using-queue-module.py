#stacks implementation using queue module

'''
push ---> put method
pop  ---> get method
'''


import queue
stack = queue.LifoQueue(3) #index to give the exact length of stack
stack.put(10) # to append the values to queue
stack.put(20)
stack.put(30)

print(stack)

print("removing values from queue...")
print(stack.get()) # to remove the value from queue
print(stack.get())

print(stack)

print("appending more values...")

stack.put(40)
stack.put(50)

print("done!")

#stack.put(69, timeout=3)    #timeout to break the execution of program

print(stack.get(timeout=2))
print(stack.get(timeout=2))
print(stack.get(timeout=2))

#print(stack.get(timeout=2))  #timeout to break the execution of program



