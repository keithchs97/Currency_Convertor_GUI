import requests
import json
import os

FILEPATH = 'symbols.txt'


def read_file(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:  # read an external file with exception handling
        symbols_local = file_local.readlines()
    return symbols_local


api_key = {"apikey": "zG00dCavzdlLN6J7ItRDRa5CYaG4v5NO"}
url = "https://api.apilayer.com/exchangerates_data/symbols"
response = requests.request("GET", url, headers=api_key)


def currency_convertor(base, target, amount):
    url_convertor = f"https://api.apilayer.com/exchangerates_data/latest?symbols={target}&base={base}"
    response_convertor = requests.request("GET", url_convertor, headers=api_key)
    result_convertor = response_convertor.json()
    converted_amount = int(result_convertor['rates'][target]) * amount

    return(f"{base} --> {target} rate = {result_convertor['rates'][target]}\n"
           f"{amount} {base} is equal to {converted_amount} {target} based on latest exchange rates.")
