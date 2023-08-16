import os

import requests
from dotenv import load_dotenv
from PySide6.QtWidgets import QMainWindow

from ui_currency_converter import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        load_dotenv()
        
        API_KEY = os.getenv("API_KEY")
        
        GET_LATEST = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=&base_currency=EUR"
        GET_CURRENCY = f"https://api.freecurrencyapi.com/v1/currencies?apikey={API_KEY}&currencies=&base_currency=EUR"
        self.response = requests.get(GET_LATEST)
        self.latest_json = self.response.json()
        
        flag_icons = {
            'AUD' : 'AUD.png',
            'BGN' : 'BGN.png',
            'BRL' : 'BRL.png',
            'CAD' : 'CAD.png',
            'CHF' : 'CHF.png',
            'CNY' : 'CNY.png',
            'CZK' : 'CZK.png',
            'DKK' : 'DKK.png',
            'EUR' : 'EUR.png',
            'GBP' : 'GBP.png',
            'HKD' : 'HKD.png',
            'HRK' : 'HRK.png',
            'HUF' : 'HUF.png',
            'IDR' : 'IDR.png',
            'ILS' : 'ILS.png',
            'INR' : 'INR.png',
            'ISK' : 'ISK.png',
            'JPY' : 'JPY.png',
            'KRW' : 'KRW.png',
            'MXN' : 'MXN.png',
            'MYR' : 'MYR.png',
            'NOK' : 'NOK.png',
            'NZD' : 'NZD.png',
            'RON' : 'RON.png',
            'RUB' : 'RUB.png',
            'SEK' : 'SEK.png',
            'SGD' : 'SGD.png',
            'THB' : 'THB.png',
            'TRY' : 'TRY.png',
            'USD' : 'USD.png',
            'ZAR' : 'ZAR.png'
        }
        
        for key in self.latest_json['data'].keys():
            self.combo_from.addItem(key)
            self.combo_from.itemIcon()
            
        for key in self.latest_json['data'].keys():
            self.combo_to.addItem(key)
        
        
        