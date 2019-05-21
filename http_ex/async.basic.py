import time
import asyncio


async def now():
    time.sleep(1)
    return time.time()


async def do_some_work(x):
    #await now()
    await asyncio.sleep(1)
    #time.sleep(1)
    return 'Done after {}s'.format(x)


def callback(future):
    print('Callback: ', future.result())


loop = asyncio.get_event_loop()


async def main():
    tasks = []
    for _ in range(100):
        coroutine = asyncio.ensure_future(do_some_work(_))
        tasks.append(coroutine)
    res = await asyncio.gather(*tasks)

    return res

t = asyncio.ensure_future(main())
print(loop.run_until_complete(t))
