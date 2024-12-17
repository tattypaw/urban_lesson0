import time
import asyncio

async def notification():
    time.sleep(10)
    print("Wait 10 minutes for delivery")

async def main():
    task = asyncio.create_task(notification())
    print("Going to come away")
    print("Go")

asyncio.run(main())