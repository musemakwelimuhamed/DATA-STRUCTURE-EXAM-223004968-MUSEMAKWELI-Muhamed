class HotelOrderQueue:
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        
        return self.front == -1
    
    def is_full(self):
        
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, order):
        if self.is_full():
            
            print("Queue is full, overwriting the oldest order.")
            self.front = (self.front + 1) % self.capacity  
        
        if self.is_empty():
            
            self.front = self.rear = 0
        else:
            
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order
        print(f"Order added: {order}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, no orders to process.")
            return None
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            
            self.front = (self.front + 1) % self.capacity
        
        print(f"Order processed: {order}")
        return order
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty, no orders to show.")
            return None
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Queue is empty, no orders to display.")
            return
        print("Current orders in the queue:")
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
queue = HotelOrderQueue(5)  
queue.enqueue("Order 1: Room 101 - Review: 5 stars")
queue.enqueue("Order 2: Room 202 - Review: 4 stars")
queue.enqueue("Order 3: Room 303 - Review: 3 stars")
queue.enqueue("Order 4: Room 404 - Review: 2 stars")
queue.enqueue("Order 5: Room 505 - Review: 1 star")
queue.display()
queue.enqueue("Order 6: Room 606 - Review: 4 stars")
queue.display()
queue.dequeue()
queue.display()
print("Front order:", queue.peek())
