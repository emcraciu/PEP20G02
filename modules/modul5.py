def pinball_test(data):
    """This is a function"""
    test_data = []
    print(data)

pinball_test('function')

class PinballTest:
    """This is a class"""
    test_data = 1, 2, 3
    def __init__(self, data):
        self.var1 = []
        self.test_data = 2, 3, 4
        if len(data) > 2:
            print('long string')
        else:
            print('short string')

    def new_method(self):
        self.var4 = 4
        print('in new method')

print(PinballTest.test_data)
obj = PinballTest('data')
print(obj.test_data)
print(PinballTest.test_data)
