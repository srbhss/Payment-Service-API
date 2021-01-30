from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db
from ..models.transaction import TransactionModel
from lib.paymentGateway import PaymentGateway


class ProcessPayment(Resource):

    # this parser will going to require name, description and traduction for any transaction that will be created
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float)

    # post method to create a transaction
    @jwt_required()
    def post(self):
        data = ProcessPayment.parser.parse_args()
        current_user = current_identity

        #validation for amount value
        if ((not data['amount']) or data['amount'] <= 0):
            return {'message': "The request is Invalid"}, 400
        amount = data['amount']

        try:
            #save transaction in db
            transaction = TransactionModel(current_user.id, amount)
            transaction.save_to_db()  
        except:
            return {'message': "Error"}, 500
        else:
            try:
                # process payment
                PaymentGateway(amount).processPayment()
            except:
                # remove transaction from database if payment failed
                transaction.delete_from_db()
                return {'message': "Error"}, 500
        return {'message': "Paymenty is processed"}, 200

