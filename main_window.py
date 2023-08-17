import os

import requests
from dotenv import load_dotenv
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QLabel

from ui_currency_converter import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        load_dotenv()
        
        self.API_KEY = os.getenv("API_KEY")
        
        self.base_currency = 'EUR'
        self.base_value = ''
        
        self.to_currency = 'USD'
        self.to_value = ''
        
        self.GET_LATEST = f"https://api.freecurrencyapi.com/v1/latest?apikey={self.API_KEY}&currencies=&base_currency={self.base_currency}"
        self.GET_CURRENCY = f"https://api.freecurrencyapi.com/v1/currencies?apikey={self.API_KEY}&currencies=&base_currency={self.base_currency}"
        
        self.latest_response = requests.get(self.GET_LATEST)
        self.latest_json = self.latest_response.json()
        
        self.currency_response = requests.get(self.GET_CURRENCY)
        self.currency_json = self.currency_response.json()
        
        self.exchange_rate_amount.setText('')
        
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
            'PHP' : 'PHP.png',
            'PLN' : 'PLN.png',
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
            icon_path = os.path.join('images', flag_icons[key])
            icon = QIcon(icon_path)
            self.combo_from.addItem(icon, key)

        for key in self.latest_json['data'].keys():
            icon_path = os.path.join('images', flag_icons[key])
            icon = QIcon(icon_path)
            self.combo_to.addItem(icon, key)
        
        self.combo_from.setCurrentText(self.base_currency)
        self.combo_to.setCurrentText(self.to_currency)
        
        self.combo_from.currentIndexChanged.connect(self.combo_from_changed)
        self.combo_to.currentIndexChanged.connect(self.combo_to_changed)
        
        self.convert_button.clicked.connect(self.convert_button_clicked)
        
    def get_latest(self, api_key, base_currency):
        self.GET_LATEST = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies=&base_currency={base_currency}"
        
        self.latest_response = requests.get(self.GET_LATEST)
        self.latest_json = self.latest_response.json()    
    
    def combo_from_changed(self, index):
        self.base_currency = self.combo_from.currentText()
        
        self.get_latest(self.API_KEY, self.base_currency)

        self.base_value = float(self.latest_json['data'][self.base_currency])
        
    def combo_to_changed(self, index):
        self.to_currency = self.combo_to.currentText()
        self.to_value = float(self.latest_json['data'][self.to_currency])
    
    def convert_button_clicked(self):
        amount = float(self.amount_line_edit.text())
        exchange_rate = float(self.latest_json['data'][self.to_currency])
        target_currency = str(round((amount * exchange_rate), 2))
        
        text_symbol = self.currency_json['data'][self.to_currency]['symbol']

        self.exchange_rate_amount.setText(f"{text_symbol} {target_currency}")