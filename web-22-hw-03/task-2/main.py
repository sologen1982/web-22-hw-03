import time
from multiprocessing import Pool, cpu_count

def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(number):
    factors = []
    pool = Pool(cpu_count())
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    pool.close()
    pool.join()
    return factors

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def factorize(*numbers):
    results = []
    for number in numbers:
        result, execution_time = measure_time(factorize_sync, number)
        results.append((result, execution_time))
    return results

a, b, c, d = factorize(128, 255, 99999, 10651060)

print("128:", a)
print("255:", b)
print("99999:", c)
print("10651060:", d)

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]