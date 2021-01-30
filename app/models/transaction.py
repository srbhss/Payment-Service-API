from db.database import db


# transaction model
class TransactionModel(db.Model):

    # transactions table configuration
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Float)
    amount = db.Column(db.String(100))

    # constructor
    def __init__(self, userId, amount):
        self.userId = userId
        self.amount = amount

    # save a transaction into db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete a transaction from the db
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
