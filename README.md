# Kasa Power Switch connected to Internet Modem

## Preface Notes

Can be saved to any Linux OS but a Raspberry Pi acts as a great host for this. 

# Install all PyPi modules

## python-kasa
## asyncio
## logging

# Use Discover to find Name and IP of Switch

Run discovery_kasa.py

# Edit Switch IP in Main Script

Inside kasa_modem.py, edit the hostname to match your designated IP address for the preferred power switch

async def kasa_modem(hostname = "10.0.0.62"):

# Cron Script
Prefer to run every 8 minutes but adjust to your needs
Adjust to your specific location of Python as well!

*/8 * * * * /home/pi/.venvs/env/bin/python /opt/kasa_modem/kasa_modem.py
