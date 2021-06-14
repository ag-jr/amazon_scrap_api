from datetime import date

class Data:

    @staticmethod
    def get_data():
        data = date.today()
        return f'{data.day}/{data.month}/{data.year}'
