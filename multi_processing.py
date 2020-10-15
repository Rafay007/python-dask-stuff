import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed

start = time.perf_counter()

def do_something(seconds:int , name:str)->str:
    time.sleep(seconds)
    return 'done sleeping '+name


# with ProcessPoolExecutor(max_workers=100) as executor:
#     results = [executor.submit(do_something,1,'hi') for _ in range(100)]
#     for f in as_completed(results):
#         print(f.result())

from functools import partial

func = partial(do_something, 1)
with ProcessPoolExecutor(max_workers=100) as executor:
    results = executor.map(func,['s' for i in range(100)] )
    for result in results:
        print(result)
# before python 3
# processes = []
# for _ in range(30):
#     p = multiprocessing.Process(target=do_something,args=[1.5])
#     p.start()
#     processes.append(p)
#
# for i in range(30):
#     processes[i].join()
#
#
finish = time.perf_counter()

print(f'\n\n finished in  {round(finish-start,2)} seconds')




