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
        
        API_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
        self.response = requests.get(API_URL)
        self.currency_info = self.response.json()
        print(self.currency_info)
        