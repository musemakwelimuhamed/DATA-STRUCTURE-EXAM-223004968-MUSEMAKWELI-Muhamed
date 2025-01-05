
class Review:
    def __init__(self, hotel, rating, comment):
        self.hotel = hotel
        self.rating = rating
        self.comment = comment
        self.next = None
        self.prev = None

class HotelSystem:
    def __init__(self):
        self.heap = []
        self.head = None
        self.tail = None
    
    def add_review(self, hotel, rating, comment):
        
        new_review = Review(hotel, rating, comment)
        
        
        if not self.head:
            self.head = new_review
            self.tail = new_review
        else:
            new_review.prev = self.tail
            self.tail.next = new_review
            self.tail = new_review
        
        
        self.heap.append([rating, hotel])
        self.heap.sort(reverse=True)
    
    def show_reviews(self):
        current = self.head
        while current:
            print(f"Hotel: {current.hotel}")
            print(f"Rating: {current.rating}")
            print(f"Comment: {current.comment}")
            print("-" * 30)
            current = current.next
    
    def show_top_hotels(self, n=3):
        print(f"Top {n} Hotels:")
        for i in range(min(n, len(self.heap))):
            print(f"Hotel: {self.heap[i][1]}, Rating: {self.heap[i][0]}")


system = HotelSystem()


system.add_review("Hilton", 4, "Good service")
system.add_review("Marriott", 5, "Excellent")
system.add_review("Holiday Inn", 3, "Average")


print("All Reviews:")
system.show_reviews()


print("\nTop Rated Hotels:")
system.show_top_hotels()