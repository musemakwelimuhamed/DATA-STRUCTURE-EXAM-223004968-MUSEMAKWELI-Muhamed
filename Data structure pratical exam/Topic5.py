class AVLNode:
    def __init__(self, hotel_id, hotel_name, rating, review):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.rating = rating
        self.reviews = [review]  
        self.avg_rating = rating  
        self.height = 1
        self.left = None
        self.right = None

class HotelReviewAVL:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, hotel_id, hotel_name, rating, review):
        def _insert(node, hotel_id, hotel_name, rating, review):
            
            if not node:
                return AVLNode(hotel_id, hotel_name, rating, review)
            
            if hotel_id < node.hotel_id:
                node.left = _insert(node.left, hotel_id, hotel_name, rating, review)
            elif hotel_id > node.hotel_id:
                node.right = _insert(node.right, hotel_id, hotel_name, rating, review)
            else:
                
                node.reviews.append(review)
                total_ratings = sum([node.rating] + [rating])
                node.avg_rating = total_ratings / (len(node.reviews))
                return node
            
            
            self.update_height(node)
            
            
            balance = self.balance_factor(node)
            
            
            if balance > 1 and hotel_id < node.left.hotel_id:
                return self.right_rotate(node)
            
        
            if balance < -1 and hotel_id > node.right.hotel_id:
                return self.left_rotate(node)
            
            
            if balance > 1 and hotel_id > node.left.hotel_id:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            
            
            if balance < -1 and hotel_id < node.right.hotel_id:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
            return node
        
        self.root = _insert(self.root, hotel_id, hotel_name, rating, review)
    
    def search(self, hotel_id):
        def _search(node, hotel_id):
            if not node or node.hotel_id == hotel_id:
                return node
            
            if hotel_id < node.hotel_id:
                return _search(node.left, hotel_id)
            return _search(node.right, hotel_id)
        
        result = _search(self.root, hotel_id)
        if result:
            return {
                'hotel_id': result.hotel_id,
                'hotel_name': result.hotel_name,
                'average_rating': result.avg_rating,
                'reviews': result.reviews
            }
        return None
    
    def inorder_traversal(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [{
                'hotel_id': node.hotel_id,
                'hotel_name': node.hotel_name,
                'average_rating': node.avg_rating,
                'review_count': len(node.reviews)
            }] + _inorder(node.right)
        
        return _inorder(self.root)


if __name__ == "__main__":
    hotel_system = HotelReviewAVL()
    
    
    hotel_system.insert(101, "Grand Hotel", 4.5, "Excellent service and amenities")
    hotel_system.insert(102, "Seaside Resort", 4.0, "Beautiful ocean view")
    hotel_system.insert(101, "Grand Hotel", 3.5, "Good but expensive")
    hotel_system.insert(103, "Mountain Lodge", 5.0, "Perfect mountain retreat")
    
    
    hotel_info = hotel_system.search(101)
    if hotel_info:
        print(f"Hotel: {hotel_info['hotel_name']}")
        print(f"Average Rating: {hotel_info['average_rating']:.1f}")
        print("Reviews:")
        for review in hotel_info['reviews']:
            print(f"- {review}")
    
    
    print("\nAll Hotels:")
    for hotel in hotel_system.inorder_traversal():
        print(f"{hotel['hotel_name']}: {hotel['average_rating']:.1f} ({hotel['review_count']} reviews)")