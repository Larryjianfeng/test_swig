import asyncio
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time


executor = ThreadPoolExecutor(max_workers=100)


def get_wait(x):
    time.sleep(3)
    return 1
'''
 submit(fn, *args, **kwargs)¶
        Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future object representing the execution of the callable.

'''

process = [executor.submit(get_wait) for _ in range(100)]

# all not done
for s in process:
    print(s.done())

time.sleep(3)

# all done
for s in process:
    print(s.done())

# all done and not delay between last and this step
for s in as_completed(process):
    print(s.result())


# the other way to conduct multi-processing
process2 = executor.map(get_wait, range(100))
for s in process2:
    print(s)
