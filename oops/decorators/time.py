import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer  #decorator
def exam_func(n):
    time.sleep(n)

exam_func(2)