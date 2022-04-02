from decimal import Decimal
from datetime import timedelta, datetime 
import itertools
from collections import namedtuple
import unittest



class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        """ this a function that when create a new intance called automatically
         """           
        self.name = name    
        self.offset = timedelta(hours=offset_hours, minutes=offset_minutes) 

class Account:
    transaction_counter = itertools.count(100)
    interest_rate = 0.5  # percent
    transaction_codes = {
        'deposit' : 'D',
        'withdraw' : 'W',
        'interest' : 'I',
        'rejected' : 'X'
    }
    
    def __init__(self, account_number, first_name, last_name,
                timezone = None, balance = Decimal('0.0')):
        """
        create a new instance from 'Account' class that have 
        account number,
        first_name of owner,
        last_name of owner,
        timezone that set 'None' by default but if you don't change it time zone will be tehran 
        and balace of account
        """
        self.first_name = self.validate_name(first_name, 'First Name')
        self.last_name = self.validate_name(last_name, 'Last Name')
        self.account_number = account_number
        self._balance = balance
        
        
        if timezone is None:
            self.timezone = TimeZone('Tehran', 3, 30)
        elif not isinstance(timezone, TimeZone):
            raise ValueError('Time Zone must be a valid TimeZone object')
        else:
            self.timezone = timezone # use timezone that was specified when instantiating

    @property
    def fullname(self):
        return self.first_name + ' ' + self.last_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < Decimal('0.0'):
            raise ValueError('initial balance must be a non-negative value')
        self._balance = value

    def generate_confirmation_code(self, transaction_code):
        transaction_id = next(Account.transaction_counter)
        dt_str = (datetime.utcnow()).strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{transaction_id}'
    
    
    def validate_name(self, value, field_title):
        """ 
        if you don't specify value or value equals to an empty string this function return a value error.
        if not, it returns value without beginning and ending spaces
        """
        if len(str(value).strip()) == 0 or value is None:
            raise ValueError(f'{field_title} cannot be empty')
        return str(value).strip()
    
    
    def deposit(self, value):
        """
        if amount of deposite was negative, this function raise value error 
        if not, it uses 'generate_confirmation_code' to create a confirmation code 
        then add value to balance of account
        """
        if value < Decimal('0.0'):
            raise ValueError('Deposit value must be a positive number')
        
        conf_code = self.generate_confirmation_code(Account.transaction_codes['deposit'])
        self.balance += value # add value to balance 
        return conf_code
    
    def withdraw(self, value):
        """
        if amount of deposite was negative, this function raise value error 
        if your stock wasn't enough, this function rejected transaction
        if not, it uses 'generate_confirmation_code' to create a confirmation code 
        then reduce value from balance 
        """
        flag = False
        if value < Decimal('0.0'):
            raise ValueError('withdraw value must be a positive number')
        if self.balance - value < Decimal('0.0'):
            transaction_code = Account.transaction_codes['rejected']
        else:
            transaction_code = Account.transaction_codes['withdraw']
            flag = True
        conf_code = self.generate_confirmation_code(transaction_code)
        if flag:
            self.balance -= value # reduce value from balance 
        return conf_code
    
    def pay_interest(self):
        """
        function to claculate interest and add interest to balance 
        """
        interest = self.balance * Account.interest_rate / 100
        conf_code = self.generate_confirmation_code(Account.transaction_codes['interest'])
        self.balance += interest
        return conf_code

    def confirmation_code_parser(self, conf_code):
        """ seperate each part of confirmation code to gain information about transaction"""
        time_utc = datetime.strptime(conf_code.split('-')[2],'%Y%m%d%H%M%S') # time utc 
        local_time = time_utc + self.timezone.offset # local time 
        Result = namedtuple('Result' ,'transaction_code account_number time_utc transaction_id time')
        result = Result(conf_code.split('-')[0], conf_code.split('-')[1], time_utc, conf_code.split('-')[3], local_time)
        return result 

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class TestAccount(unittest.TestCase):
    def test_create_timezone_1(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_create_timezone_2(self):
        tz = TimeZone('ABC', 1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=1, minutes=-30), tz.offset)
        
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        
        a = Account(account_number, first_name, last_name, tz, balance)
        
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
    def test_create_account_blank_first_name_2(self):
        account_number = 'A100'
        first_name = '  '
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
    def test_create_account_negative_balance(self):
        account_number = 'A100'
        first_name = '  '
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('-100')
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
            
    def test_account_withdraw_ok(self):
        account_number = 'A100'
        first_name = 'First'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.withdraw(20)
        self.assertTrue(conf_code.startswith('W-'))
        self.assertEqual(balance-Decimal('20'), a.balance)

    def test_confirmationcodeparser_accountNumber(self):
        account_number = 'A100'
        first_name = 'First'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.withdraw(20)
        result = a.confirmation_code_parser(conf_code)
        self.assertEqual('A100', result.account_number)

    def test_confirmationcodeparser_timezone(self):
        account_number = 'A100'
        first_name = 'First'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        a = Account(account_number, first_name, last_name, tz, balance)
        conf_code = a.withdraw(20)
        result = a.confirmation_code_parser(conf_code)
        print(f'local time: {result.time}')
        print(f'time_utc:{result.time_utc}')

    def test_getfullname(self):
        account_number = 'A100'
        first_name = 'First'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = Decimal('100')
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual('First LAST', a.fullname)

run_tests(TestAccount)