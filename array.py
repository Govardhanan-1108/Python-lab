class Node:
    def _init_(self,data):
        self.data=value
        self.data=None
class Queue:
    def _init_(self):
        self.front=none
        self.rear=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.rear is None:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        print("",value,"added to the queue")
    def dequeue(self):
        if self.front is None:
            print("queue is empty")
        else:
            removed=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
                print("",removed,"remove from the queue")
            def display(self):
                if self.front is None:
                    print("queue is empty")
                else:
                    temp=self.front
                    print("queue",end="-->")
                    while temp is not none:
                        print(temp,data,end="-->")
                    print("Null")
q=queue()
while true:
    print("\n Main menu")
    print("1.enqueue")
    print("2.dequeue")
    print("3.display")
    print("4.exit")
    print("Enter your choice")
    ch=input("Enter the value")
    if ch=='1':
        value=input("Enter the value")
        q.enqueue(value)
    elif ch=='2':
        q.dequeue()
    elif ch=='3':
        q.display()
    elif ch=='4':
        print("program ended")    
        break
    else:
        print("Enter the valid input")
