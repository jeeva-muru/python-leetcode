class Stack:   

    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item=self.items.pop()
        return item
    
    def size(self):
        size=len(self.items)
        return size

    
    def display(self):
        for item in self.items:
            print(item)

class Queue:
    def __init__(self):
        self.inbox=Stack()
        self.outbox=Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        self.populate()
        if(self.outbox.size()!=0):
            item = self.outbox.pop()
            return item

    def peek(self):
        self.populate()
        if(self.outbox.size()!=0):
            item = self.outbox.pop()
            self.outbox.push(item)
            return item
        

    def populate(self):
        if(self.outbox.size()==0):
            size = self.inbox.size()
            if(size!=0):
                for index in range(size):
                    self.outbox.push(self.inbox.pop())

# stack = Stack()
# while True:
#     print("1:Push items")
#     print("2:Pop items")
#     print("3:display items")
#     print("4:exit")
#     choice=int(input("enter the choice:"))

#     if(choice==1):
#         item = int(input("enter the item:"))
#         stack.push(item)
#     elif(choice==2):
#         item = stack.pop()
#         print(item)
#     elif(choice==3):
#         stack.display()
#     elif(choice==4):
#         break
        
queue = Queue()

query=input()
query_list = query.split(',')
#print(query_list)
#1 42, 2,1 14, 3
#1 - enqueue, 2- dequeue, 3-peek/print
temp=[]
for i in range(len(query_list)):
    temp = query_list[i].split(' ')
    # print(temp)
    # print(temp[0])
    if (temp[0] == '1'):
        queue.enqueue(temp[1])
    elif (temp[0] == '2'):
        queue.dequeue()
    elif (temp[0] == '3'):
        print(queue.peek())