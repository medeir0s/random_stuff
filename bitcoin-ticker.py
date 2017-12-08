#!/usr/bin/python3

import json
import urllib.request
import subprocess as s
import time

'''
Mostra o valor atual do BTC de 5 em 5 minutos na tela, pelo notify-send
'''
def ticker():
	jsonurl = urllib.request.urlopen('https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC')
	text = json.loads(jsonurl.read().decode('utf-8'))
	buy = str(text['buy'])
	sell = str(text['sell'])
	arg = "Compra: "+buy+"  Venda: "+sell
	s.call(['notify-send',arg])
	time.sleep(300)

while True:
	try:
		ticker()	
	except:
		time.sleep(60)
		ticker()
