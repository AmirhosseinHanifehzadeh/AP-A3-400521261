# ---------------- import modules ----------------- 
from datetime import datetime
from geopy import distance
import csv
import unittest

# ---------------- medadrangi class -------------------
class MedadRangi:
    off_rate = 0.1
    product_list = [] 
    market_coordinate = (51.50185488303431, 35.74317403843504)
    
    def __init__(self, name, price, number, countrymaker, companyName):
        self.name = name 
        self.price = price 
        self.number = number
        self.countrymaker = countrymaker
        self.companyName = companyName 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError('name should be str')
        elif len(val.strip()) == 0 or val is None:
            raise ValueError 
        self._name = val
    
    @property
    def countrymaker(self):
        return self._countrymaker

    @countrymaker.setter
    def countrymaker(self, val):
        if not isinstance(val, str):
            raise TypeError('countrymaker should be str')
        elif len(val.strip()) == 0 or val is None:
            raise ValueError
        self._countrymaker = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if not isinstance(val, int):
            raise TypeError('price should be str')
        elif val <= 0:
            raise ValueError('price should be bigger than 0')
        
        self._price = val

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, val):
        if not isinstance(val, int):
            raise TypeError('number should be str')
        elif val <= 0:
            raise ValueError('number should be bigger than 0')
        self._number = val

    @property
    def companyName(self):
        return self._companyName

    @companyName.setter
    def companyName(self, val):
        if len(val.strip()) == 0 or val is None:
            raise ValueError
        self._companyName = val


    def final_price(self):
        return (1 - MedadRangi.off_rate) * self.number * self.price

    @classmethod
    def calculate_distance(cls, destination_langitude, destination_latitude):
        destination_coordinates = (destination_langitude, destination_latitude)
        return distance.distance(cls.market_coordinate, destination_coordinates).km

    @staticmethod
    def welcome():
        if 12 < datetime.now().hour < 18:
            return 'good afternoon!'
        elif 6 < datetime.now().hour <= 12:
            return 'good morning'

    @classmethod
    def load_csv(cls):
        with open('products.csv', 'r') as csv_files:
            csv_reader = csv.reader(csv_files)

            for line in csv_reader:
                cls.product_list.append({
                    'product': line[0],
                    'price': line[1],
                    'made in': line[2],
                    'maker':line[3]
                })



def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# --------------------------- testing class ---------------------------
class Test(unittest.TestCase):
    def test_instantainting_1(self):
        name = 'medad'
        price = 'hezar toman'
        number = 2
        countrymaker = 'China'
        company = 'nike'

        with self.assertRaises(TypeError):
            a = MedadRangi(name, price, number, countrymaker, company)
    
    def test_instanatiating_2(self):
        name = 123
        price = 1000
        number = 2
        countrymaker = 'China'
        company = 'nike'

        with self.assertRaises(TypeError):
            a = MedadRangi(name, price, number, countrymaker, company)

    def test_instantaiting_3(self):
        name = 'medad'
        price = 10000
        number = 2
        countrymaker = 567
        company = 'nike'

        with self.assertRaises(TypeError):
            a = MedadRangi(name, price, number, countrymaker, company)

    def test_instantiating_4(self):
        name = 'medad'
        price = 10000
        number = 2
        countrymaker = 'China'
        company = 'nike'

        a = MedadRangi(name, price, number, countrymaker, company)

        self.assertEqual(a.name , 'medad')

    def test_isntantiating_5(self):
        name = ''
        price = 10000
        number = 2
        countrymaker = 'China'
        company = 'nike'

        with self.assertRaises(ValueError):
            a = MedadRangi(name, price, number, countrymaker, company)

    def test_instantiating_6(self):
        name = 'medad'
        price = -120
        number = 2
        countrymaker = 'China'
        company = 'nike'

        with self.asssertRaises(ValueError):
            a = MedadRangi(name, price, number, countrymaker, company) 


    def test_instantiating_7(self):
        name = 'medad'
        price = 120
        number = 0
        countrymaker = 'China'
        company = 'nike'

        with self.assertRaises(ValueError):
            a = MedadRangi(name, price, number, countrymaker, company)


    def test_instantiating_8(self):
        name = 'medad'
        price = 120
        number = 1
        countrymaker = 'China'
        company = '  '

        with self.assertRaises(ValueError):
            a = MedadRangi(name, price, number, countrymaker, company)


    def test_instantiating_9(self):
        name = 'medad'
        price = 120
        number = 1
        countrymaker = 'China'
        company = 'nike'

        a = MedadRangi(name, price, number, countrymaker, company)

        self.assertEqual(a.name, name)
        self.assertEqual(a.price, price)
        self.assertEqual(a.number, number)
        self.assertEqual(a.countrymaker, countrymaker)
        self.assertEqual(a.companyName, company)
    

    def test_instantiating_6(self):
        name = 'medad'
        price = -120
        number = 2
        countrymaker = 'China'
        company = 'nike'

        with self.assertRaises(ValueError):
            a = MedadRangi(name, price, number, countrymaker, company)    


    def test_finallPrice_1(self):
        name = 'medad'
        price = 10000
        number = 2
        countrymaker = 'China'
        company = 'nike'

        a = MedadRangi(name, price, number, countrymaker, company)

        finallPrice = a.final_price()
        self.assertEqual(finallPrice, 18000)

    def test_welcome_1(self):
        name = 'medad'
        price = 10000
        number = 2
        countrymaker = 'China'
        company = 'nike'

        a = MedadRangi(name, price, number, countrymaker, company)

        CurrentHour = datetime.now().hour
        first_message = 'good morning'
        second_message = 'good afternoon!'
        method_message = MedadRangi.welcome()
        if  12 < CurrentHour < 18:
            self.assertEqual(method_message, second_message)
        elif CurrentHour <= 12:
            self.assertEqual(method_message, first_message)

run_tests(Test)

