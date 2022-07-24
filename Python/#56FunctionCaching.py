#Function Caching - The Computer saves the input and output value. And, if someone run the same thing again it gives the stored value to save the time.
import time
from functools import lru_cache

@lru_cache(maxsize=5)
def some_work(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print('Running...')
    some_work(3)
    print('Running...')
    some_work(3) #Now if I run this It'll take alot of time. If I want to save my time I can use function caching.
    print('Done...')