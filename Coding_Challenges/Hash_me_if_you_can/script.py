from lxml import html
import requests
import hashlib

cookie = {'PHPSESSID' : 'gvrl04geq5bfta21ag1tmcse55'}
page = requests.get('https://ringzer0ctf.com/challenges/13', cookies = cookie)
tree = html.fromstring(page.content)
msg = tree.xpath('/html/body/div[2]/div/div[2]/div/text()[2]').pop().strip()
print(msg)

msg=msg.encode('utf-8')
hashedMessage = hashlib.sha512(msg).hexdigest()
data = requests.get('https://ringzer0ctf.com/challenges/13/'+hashedMessage, cookies=cookie)
print("")
new_tree = html.fromstring(data.content)
flag = new_tree.xpath('/html/body/div[2]/div/div[2]/div/text()[1]')[0]
print(flag)