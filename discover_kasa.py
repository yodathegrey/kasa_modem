#!/home/pi/.venvs/env/bin/python
from kasa import Discover, Credentials, Module, Device
import asyncio
import socket
import datetime
import logging
import logging.handlers
import time


async def kasa_discover():
    dev = await Discover.discover()

    for i, k in dev.items():
        print(f"{i} [+] {k}")



def main():
    asyncio.run(kasa_discover())

if __name__ == "__main__":
    main()
