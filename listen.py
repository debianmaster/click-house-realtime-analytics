import asyncio
from nats.aio.client import Client as NATS
from clickhouse_driver import Client as ClickHouseClient
import json

async def run():
    # Connect to NATS
    nc = NATS()
    await nc.connect("127.0.0.1:4222")

    # Connect to ClickHouse with authentication
    clickhouse_client = ClickHouseClient(
        host='10.43.191.78',
        user='default',
        password='mypassword',
        database='default'
    )


    async def message_handler(msg):
        data = msg.data.decode()
        print(f"Received a message: {data}")

        result = clickhouse_client.execute('show databases;')
        print("RESULT: {0}: {1}".format(type(result), result))
        # Parse the data (assuming JSON format for simplicity)
        record = json.loads(data)
        print("------------------------------------->")
        # Insert data into ClickHouse
        clickhouse_client.execute(
            "INSERT INTO mytable (id, message) VALUES",
            [(record['id'], record['message'])]
        )

    # Subscribe to a NATS subject
    await nc.subscribe("updates", cb=message_handler)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.run_forever()