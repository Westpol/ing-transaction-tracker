from datetime import datetime


class Transaction:
    def __init__(self, date:datetime, transaction_name:str, details:str, payment:float, currency_payment:str, balance:float , currency_balance:str, type:str, raw_data:str):
        self.date = date
        self.transaction_name = transaction_name
        self.details = details
        self.payment = payment
        self.currency_payment = currency_payment
        self.balance = balance
        self.currency_balance = currency_balance
        self.type = type
        self.raw_data = raw_data

    def get_date(self) -> datetime:
        return self.date

    def get_details(self) -> str:
        return self.details

    def get_transaction_name(self) -> str:
        return self.transaction_name

    def get_payment(self) -> float:
        return self.payment

    def get_currency_payment(self) -> str:
        return self.currency_payment

    def get_balance(self) -> float:
        return self.balance

    def get_currency_balance(self) -> str:
        return self.currency_balance

    def get_type(self) -> str:
        return self.type

    def get_raw_data(self) -> str:
        return self.raw_data

    def print_object(self) -> str:
        return str(datetime.strftime(self.date, "%d.%m.%Y")) + "    " + self.transaction_name + "    " + str(self.payment) + " " + self.currency_payment + "    " + self.details