class Terminal:
    def __init__(self, number, pin) -> None:
        '''Номер карточки должен содержать 16 цифр(писать слитно),
           PIN-код должен содержать 4 цифры'''

        if len(str(number)) != 16:
            raise ValueError('Номер карточки должен содержать 16 цифр!')
        if len(str(pin)) != 4:
            raise ValueError('PIN-код должен содержать 4 цифры!')
        self.__number = number
        self.__pin = pin
        self.balance = 0

    def check_pin(self, pin):
        if pin != self.__pin:
            raise ValueError('PIN-код не совпадает!')
            

    def put(self, pin, value):
        self.check_pin(pin)
        self.balance += value
        return f'Зачислено {value}\nСумма на карте: {self.balance}'

    def get_money(self, pin, value):
        self.check_pin(pin)
        
        if value % 10 != 0:
            raise ValueError('Принимаются только округленные суммы: 10, 50, 100, 500, 1000 и тд.')
        
        if self.balance == 0 or self.balance < value:
            raise TypeError('Недостаточно средств')
        
        self.balance -= value
        return f'Выдано: {value}\nОстаток на карте: {self.balance}'
    

my_akk = Terminal(1234123412341234, 1345)
print(my_akk.put(1345, 9000))
print(my_akk.put(1345, 5000))
print(my_akk.get_money(1345, 300))


    



