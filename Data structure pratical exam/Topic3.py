class ReviewQueue:
    def __init__(self):
        self.queue = []

    def add_review(self, hotel, rating, comment):
        review = {
            'hotel': hotel,
            'rating': rating,
            'comment': comment,
            'status': 'pending'
        }
        self.queue.append(review)
        print(f"Review added for {hotel}")

    def process_next_review(self):
        if self.queue:
            review = self.queue.pop(0)
            review['status'] = 'processed'
            print(f"Processed review for {review['hotel']}")
            return review
        return None

    def show_pending_reviews(self):
        print("\nPending Reviews:")
        for review in self.queue:
            print(f"Hotel: {review['hotel']}")
            print(f"Rating: {review['rating']}")
            print(f"Comment: {review['comment']}")
            print("-" * 20)


review_system = ReviewQueue()


review_system.add_review("Hilton", 4, "Nice stay")
review_system.add_review("Marriott", 5, "Excellent")
review_system.add_review("Holiday Inn", 3, "Average")


review_system.show_pending_reviews()


print("\nProcessing reviews:")
for _ in range(3):
    review_system.process_next_review()