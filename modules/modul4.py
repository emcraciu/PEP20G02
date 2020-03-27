"""
This is module 4 ouf our course
"""

shop1 = {'mere': 100, 'pere': 110, 'prune': 35, 'ananas': 50}
shop2 = {'mere': 110, 'pere': 100, 'prune': 30}
shop3 = {'mere': 100, 'pere': 100, 'prune': 40}
shops = [shop1, shop2, shop3]
shopping_list = {'mere': 1, 'pere': 2, 'prune': 3}


def best_buy(shops: list, shopping_list: dict):
    """Function to select best shop by price form list of shops

    :param shops: list of shops
    :param shopping_list: dictionary of items to by and there amount
    :return: dictionary representing best shop
    """
    best_price = 0
    best_shop = {}
    for shop in shops:
        shop_price = 0
        for item in shopping_list:
            shop_price += shop[item] * shopping_list[item]
        if not best_price or best_price > shop_price:
            best_price = shop_price
            best_shop = shop
        print('shop price:', shop_price)
    print('best price:', best_price)
    return best_shop

print(best_buy.__doc__)

shop = best_buy(shops, shopping_list)
print(shop)

set1 = {1, 5, 5}
set2 = {3, 8, 9}
set3 = {2, 3, 6}
set4 = {10, 5, 7}
data = [set1, set2, set3, set4]


def pinball_game_test(game_data, ful_range=10):
    range_values = set(range(1, ful_range + 1))
    ful_set = set()
    for mach_game in game_data:
        ful_set = ful_set.union(mach_game)
    return range_values.difference(ful_set)


error = pinball_game_test(data)
print(error)


def tuple_function(*args, **kwargs):
    for key, value in kwargs.items():
        print('KWARG is: {}:{}'.format(key, value))
    for arg in args:
        print(arg)


tuple_function(1, 'a', 20, {}, key1='1', something=2)

list_to_flatten = [[[1, [3, 5]], 2, 3], [4, 5], [6], 7]


def flatten_list(list_to_flatten):
    result = []
    for obj in list_to_flatten:
        if isinstance(obj, list):
            result.extend(flatten_list(obj))
        else:
            result.append(obj)
    return result


result = flatten_list(list_to_flatten)
print(result)
