#queueu implementation using lists

'''
enqueue  ---> append method / insert method
dequeu   ---> pop method
isFull
isEmpty
'''



queue = []

#appending few elements
queue.append(1)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)



queue.pop(0) # use 0 index to remove from the head/front end
print(queue)

queue.pop(0) 
print(queue)

queue.pop(0) 
print(queue)

queue.pop(0) 
print(queue)


''' or we can use insert method to append elements '''

queue.insert(0,10) #index,element
queue.insert(0,20)
queue.insert(0,30)

print(queue)
print(queue.pop())
print(queue.pop())
print(queue.pop())

