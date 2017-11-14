import hmac
import hashlib
import requests
from time import time
try:
	from urllib.parse import urlencode
except:
	from urllib import urlencode
	
class CobinhoodApiError(Exception):
	pass
	
class Cobinhood:
	def __init__(self, key=None, secret=None):
		self._key = key
		self._secret = secret
		
	def _v1(self, *args):
		url = 'https://api.cobinhood.com/v1/' + '/'.join(args)
		r = requests.get(url, verify=False)
		print(r)
		return r.json()
		
	def _api(self, **params):
		if not self._key or not self._secret:
			raise CobinhoodApiError('API keys are not configured')
		# Authentication goes here
		# Dynamic Request and Response
		
	def _sign(self, data):
		if isinstance(data, dict):
			data = urlencode(data)
		return #signature generated
	
	# Account
	def getDeviceId(self, platform):
		return requests.post('https://api.cobinhood.com/v1/account/device', data = {'platform':platform}, verify=False)
		
	# User
	def getUserInfo(self):
		return self._v1('user','info')
		
	# System
	def getSystemTime(self):
		return self._v1('system','time')
		
	def getSystemInformation(self):
		return self._v1('system','info')
		
	def getSystemMessageIds(self):
		return self._v1('system','messages')
		
	def getSystemMessage(self, messageId):
		return self._v1('system','messages', messageId)
		
	# Market
	def getAllCurrencies(self):
		return self._v1('market','currencies')

	def getAllTradingPairs(self):
		return self._v1('market','trading_pairs')
		
	def getOrderBook(self, pair):
		return self._v1('market','orderbooks', pair)
		
	def getTicker(self, pair):
		return self._v1('market','tickers', pair)
		
	def getRecentTrades(self, pair):
		return self._v1('market','trades',pair)
		
	# Chart
	def getCandles(self, pair):
		return self._v1('chart','candles', pair)
		
	# Trading
	def getOrder(self, orderId):
		return self._v1('trading','orders', orderId)
		
	def getTradesOfAnOrder(self, orderId):
		return self._v1('trading','orders',orderId,'trades')
		
		

		
	