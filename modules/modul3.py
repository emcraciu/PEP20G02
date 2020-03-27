def div(x, y):
    try:
        z = x/y
    except AttributeError:
        print('something went wrong')
    except ZeroDivisionError:
        print('do not use zero')
        raise RuntimeError
    except:
        print('last resort')
    else:
        print('all is good')
    finally:
        print('this will always be done')

print(div(10, 0))
print('success')