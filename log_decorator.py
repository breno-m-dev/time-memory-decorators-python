def log_function(func):
    """
    this function is supposed to be used as a decorator. It prints a
    message before executing a function.
    """
    def log_print(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return log_print;

# @log_function
# def print_range(length: int):
#     for i in range(length):
#         print(i)

# @log_function
# def aoba():
#     print("aoba")

# print_range(5)
# aoba()