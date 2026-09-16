import tracemalloc
from functools import wraps

def measure_memory(func):
    """
    This decorator starts measuring the memory usage of a method at the
    beggining of the execution of the method. And prints the peak memory usage
    and the final usage after execution.
    Args: func: function that will be tested
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        print(f"Current memory: {current / 1024:.2f} KB")
        print(f"Peak memory: {peak / 1024:.2f} KB")

        return result

    return wrapper