#!/home/pi/.venvs/env/bin/python
from kasa import Discover, Credentials, Module, Device
import asyncio
import socket
import datetime
import logging
import logging.handlers
import time

LOGFILE='/opt/kasa_modem/log_kasa/logkasa.log'

#Setup logger
logger = logging.getLogger('KasaLogger')
logger.setLevel(logging.INFO)

#Setup format
format =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#Setup handler
handler = logging.handlers.RotatingFileHandler(LOGFILE, maxBytes=1000000, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(format)

logger.addHandler(handler)


def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """

    #TESTING PURPOSES - uncomment line below
    #host="6.6.6.7"

    try:
        logger.info("Connecting to: {0}".format(host))
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        logger.info("Connection success!!!")
        return True
    except socket.error as ex:
        logger.info('Connection failed: {0}'.format(ex))
        return False


async def kasa_modem(hostname = "10.0.0.62"):
    creds = Credentials(username, password)

    dev = await Device.connect(host=hostname)
    await dev.update()
    logger.info("Connected to {0}: {1}".format(hostname, dev.alias))

    if dev.is_off:
        logger.info("Kasa offline... turning on now...")
        await dev.turn_on()
    else:
        logger.info("Kasa online... shutting off now...")
        await dev.turn_off()
        await dev.update()
        if dev.is_off:
            logger.info("Kasa now offline... starting back up...")
            await dev.turn_on()

    await dev.update()

    logger.info("Device: {0} - {1} online = {2}".format(dev.alias, dev.model, dev.is_on))


def main():
    logger.info("Script started...")

    #Counter
    i=0
    reset_counter=8

    #Test for internet connectivity
    while i<reset_counter and not internet():
        i+=1
        logger.info("No internet...retrying in 30 seconds.")
        time.sleep(30)

        #logger.info('i={0}'.format(i))

        if i>=reset_counter:
            logger.info("Initiating Kasa connection.")
            asyncio.run(kasa_modem())

    logger.info("Script shutting down....")

if __name__ == "__main__":
    main()
