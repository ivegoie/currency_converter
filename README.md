# Currency Exchange

Currency Exchange is a simple currency converter application implemented using Python and the PySide6 library for building graphical user interfaces. The application allows users to convert between different currencies based on the latest exchange rates obtained from an external API.s

![Currency Exchange Screenshot](https://i.ibb.co/6wd2ZmW/currency-exchange-showcase.png)

## Features

- Graphical User Interface (GUI): The application provides a user-friendly graphical interface built using the PySide6 library, making it easy for users to interact with the currency conversion functionality.

- Currency Conversion: Users can select a base currency and a target currency from dropdown lists. After entering an amount in the base currency, clicking the "Convert" button will display the equivalent value in the target currency.

- Real-time Exchange Rates: The application retrieves the latest exchange rates from an external API, specifically the "Free Currency API," which provides up-to-date currency conversion rates.

- Currency Icons: The dropdown lists for selecting currencies display icons representing each currency's flag, making it visually intuitive for users to choose currencies.

## Prerequisites

- `Python` 3.x
- `requests` library
- `dotenv` library
- `PySide6` library
- `Montserrat` font family

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ivegoie/currency_exchange.git
   cd currency_exchange
   ```

2. Install the required libraries using pip:
    ```bash
    pip install requests dotenv PySide6
    ```

3. Obtain an API key from [Free Currency API](https://app.freecurrencyapi.com/register) and store it in a .env file in the root directory of the project:
    ```env
    API_KEY=your_api_key_here
    ```
## Usage
1. Run the main.py script:
    ```bash
    python main.py
    ```
2. The application window will appear with dropdowns to select the base and target currencies, an input field to enter the amount in the base currency, and a "Convert" button.

3. Select the desired base and target currencies from the dropdowns.
Enter the amount in the base currency you want to convert.
Click the "Convert" button to see the equivalent value in the target currency.

## Currency Flag Icons

The application displays currency flag icons corresponding to country currency. The icons are located in the images directory. The appropriate icon is chosen based on the country currency.

![Currency Flag Icons](https://camo.githubusercontent.com/992b9e4b1ea55cc504a7045a44ae493760d815c2867f719c3111e4087d394d82/68747470733a2f2f692e6962622e636f2f396e35764a426d2f706978656c2d666c6167732e706e67)

## Acknowledgments
This project uses the [FreeCurrencyAPI](https://app.freecurrencyapi.com/) to fetch weather data.

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to customize, enhance, and adapt this currency converter application to your needs. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Enjoy currency conversion made simple!