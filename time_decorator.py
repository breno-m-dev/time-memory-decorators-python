import time

def timer(func):
    """
    this function is supposed to be used as a decorator. It makes every
    function to show how much time it took to be executed.
    """
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to be executed")
        return result

    return wrapper


# @timer
# def test():
#     l = 50000000
#     for i in (range(l)):
#         pass

    
# test()