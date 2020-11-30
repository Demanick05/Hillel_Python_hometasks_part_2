import uuid
from . import logs_config as record


class Review:
    def __init__(self, text, author, rating, status="Moderation"):
        record.logger.debug("Class 'Review' was created")
        self.id = uuid.uuid4()
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
