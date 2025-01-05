class HotelNode:
    def __init__(self, name, category="root"):
        self.name = name
        self.category = category
        self.rating = 0
        self.review_count = 0
        self.reviews = []
        self.children = []
class HotelHierarchy:
    def __init__(self):
        self.root = HotelNode("Hotels")
    
    def add_node(self, path, review=None, rating=None):
        current = self.root
        for i, (name, category) in enumerate(path):
            child = next((c for c in current.children if c.name == name), None)
            if not child:
                child = HotelNode(name, category)
                current.children.append(child)
            current = child
        if review and rating:
            current.reviews.append(review)
            current.rating = ((current.rating * current.review_count) + rating) / (current.review_count + 1)
            current.review_count += 1
    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        result = []
        prefix = "  " * level
        info = f"{prefix}{node.name}"
        if node.category != "root":
            info += f" ({node.category})"
        if node.review_count:
            info += f" - Rating: {node.rating:.1f} ({node.review_count} reviews)"
        result.append(info)
        for child in node.children:
            result.extend(self.display(child, level + 1))
        return result
hierarchy = HotelHierarchy()
hierarchy.add_node([
    ("USA", "country"),
    ("New York", "city"),
    ("Grand Hotel", "hotel")
], "Excellent stay", 4.5)
hierarchy.add_node([
    ("USA", "country"),
    ("New York", "city"),
    ("Grand Hotel", "hotel")
], "Good service", 4.0)
hierarchy.add_node([
    ("USA", "country"),
    ("Miami", "city"),
    ("Beach Resort", "hotel")
], "Great beach view", 5.0)
for line in hierarchy.display():
    print(line)