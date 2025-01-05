class HotelReview:
    def __init__(self, hotel_name, rating, date, priority_level):
        self.hotel_name = hotel_name
        self.rating = rating
        self.date = date
        self.priority_level = priority_level
    
    def __str__(self):
        return f"{self.hotel_name}: {self.rating}★ (Priority: {self.priority_level}, Date: {self.date})"

def bubble_sort_hotels(reviews, sort_by='priority'):
    n = len(reviews)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if sort_by == 'priority':
                condition = (reviews[j].priority_level < reviews[j + 1].priority_level or 
                           (reviews[j].priority_level == reviews[j + 1].priority_level and 
                            reviews[j].rating < reviews[j + 1].rating))
            elif sort_by == 'rating':
                condition = reviews[j].rating < reviews[j + 1].rating
            elif sort_by == 'date':
                condition = reviews[j].date < reviews[j + 1].date
            
            if condition:
                reviews[j], reviews[j + 1] = reviews[j + 1], reviews[j]
                swapped = True
        
        if not swapped:
            break
    
    return reviews
reviews = [
    HotelReview("Grand Hotel", 4.5, "2024-01-15", 2),
    HotelReview("Beach Resort", 5.0, "2024-01-10", 3),
    HotelReview("Mountain Lodge", 4.0, "2024-01-20", 1),
    HotelReview("City Center", 4.8, "2024-01-12", 3)
]
sorted_reviews = bubble_sort_hotels(reviews, 'priority')
print("Sorted by Priority:")
for review in sorted_reviews:
    print(review)
sorted_by_rating = bubble_sort_hotels(reviews, 'rating')
print("\nSorted by Rating:")
for review in sorted_by_rating:
    print(review)