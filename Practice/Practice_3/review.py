"""
Добавьте сущность Review.

Review имеет текст, автора (Customer), оценку от 1 до 5, статус (по умолчанию, "Moderation").

Customer может создать Review.

Admin может одобрить Review (статус меняется на "Published").
"""


class Review:
    def __init__(self, text, author, rating, status="Moderation"):
        self.text = text
        self.author = author
        self.rating = rating
        self.status = status

    def __str__(self):
        return f"This review belongs to {self.author}, it has a rating of {self.rating} " \
               f"and currently its status is {self.status}"

    def __repr__(self):
        return f"This review belongs to {self.author}, it has a rating of {self.rating} " \
               f"and currently its status is {self.status}"


"""
Customer for customer method of review creation looks as following:
"""


def create_review(self, text, author):
    new_review = Review(text, author)
    self.reviews.append(new_review)
    return new_review


"""
Function for Review approving looks as following:
"""


def approve_review(self):
    new_status = "Published"
    Review.status = new_status
    return Review.status