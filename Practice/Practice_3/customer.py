from .user import User
from .order import Order
from .review import Review
from . import logs_config as record


class Customer(User):
    def __init__(self, username, userpass,
                 first_name, last_name, phone, email, date_of_birth):
        super().__init__(username, userpass, email)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.bonus_amount = 0
        self.orders = list()
        self.reviews = list()

    def __str__(self):
        return f"Customer {self.id}: {self.first_name}, {self.last_name}"

    def create_order(self, item, amount):
        record.logger.info("Order created")
        new_order = Order(self, item, amount)
        self.orders.append(new_order)
        return new_order

    def create_review(self, text, author):
        record.logger.info("Review created")
        new_review = Review(text, author, rating=3)
        self.reviews.append(new_review)
        return new_review


if __name__ == "__main__":  #this will work only if this file launches directly
    c1 = Customer("Guido", "Van Rossum", "000-112-35-8", "guido@python.org"
                                                         "09-09-1968")
