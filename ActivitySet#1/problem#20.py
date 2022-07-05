from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


y = lst()

ctx = openssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = openssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


tags = soup('stan')
for tag in tags:
    number = re.findall('\".([0-9]+).+', line)
    for k in number:
        y.append(int(k))
        print(sum(y))