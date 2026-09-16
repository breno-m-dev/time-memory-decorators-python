import log_decorator
import time_decorator
import memory_decorator

@time_decorator.timer
@memory_decorator.measure_memory
def big_list():
    list = []
    for i in (range(50000000)):
        list.append(i)

big_list()