import asyncio
from nats.aio.client import Client as NATS
import json

async def run():
    nc = NATS()
    await nc.connect("127.0.0.1:4222")

    # Sample message
    message = {
        "id": 1,
        "message": "Hello, ClickHouse!",
        "timestamp": "2024-05-29 10:00:00"
    }

    await nc.publish("updates", json.dumps(message).encode())
    await nc.flush()

    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())