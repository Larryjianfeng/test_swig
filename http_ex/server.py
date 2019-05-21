import asyncio
from aiohttp import web
from concurrent.futures import ThreadPoolExecutor


async def model(x):
    await asyncio.sleep(x)
    return x


async def post_handler(request):
    data = await asyncio.wait_for(request.json(), 10)
    ret = await model(data['x'])
    ret_body = {'ret': ret}
    return web.Response(body=ret_body)


loop = asyncio.get_event_loop()


async def init(loop):
    handler_args = {"tcp_keepalive": False, "keepalive_timeout": 25}
    app = web.Application(loop=loop,
                          client_max_size=10**10,
                          handler_args=handler_args)
    app.router.add_route('post', '/gnes', post_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8070)
    await site.start()


loop.run_until_complete(init(loop))
loop.run_forever()