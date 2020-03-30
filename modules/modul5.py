# def pinball_test(data):
#     """This is a function"""
#     test_data = []
#     print(data)
#
# pinball_test('function')
#
# class PinballTest:
#     """This is a class"""
#     test_data = 1, 2, 3
#     def __init__(self, data):
#         self.var1 = []
#         self.test_data = 2, 3, 4
#         if len(data) > 2:
#             print('long string')
#         else:
#             print('short string')
#
#     def new_method(self):
#         self.var4 = 4
#         print('in new method')
#
# print(PinballTest.test_data)
# obj = PinballTest('data')
# print(obj.test_data)
# print(PinballTest.test_data)


# class A():
#     A = 'A'
#     def __init__(self):
#         pass
#
#     def a(self):
#         print('a')
#
# class B(A):
#     A = 'B'
#
#     def a(self):
#         print('b')
#
# class C(A, B):
#
#     def a(self, value):
#         print(value)
#
# c = C()
# print(c.A)

# a = input('val:')
# var = 1 if int(a) < 3 else 2
# print(var)


# var1 = [i for i in range(10)]
# print(var1)

# var2 = (i for i in range(10))
# print(var2)
# print(next(var2))

# def new_gen(max):
#     for i in range(max):
#         yield i
#
# var4 = new_gen(100000000000000000000)
#
# for i in range(10):
#     print(next(var4))

class PrimesIter():

    def __init__(self, primes_list: list):
        self.primes_list = primes_list

    def __next__(self):
        if len(self.primes_list) == 0:
            raise StopIteration
        return self.primes_list.pop(0)

    def __iter__(self):
        return self

class Primes():

    def __init__(self):
        self.primes = []
        for x in range(1, 10000):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                self.primes.append(x)

    def __iter__(self):
        return PrimesIter(self.primes)

primes = Primes()
var1 = iter(primes)
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))

print(next(var1))