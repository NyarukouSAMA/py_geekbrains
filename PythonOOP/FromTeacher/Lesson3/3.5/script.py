import requests
import json

def get_iata_code(city):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20" + city + "%20в%20Лондон"
    text = requests.get(link).text
    data = json.loads(text)
    iata = data["origin"]["iata"]
    return iata

origin = get_iata_code(input("Введите город отправления:"))
dest = get_iata_code(input("Введите город прибытия:"))
link = "http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin="+origin+"&destination="+dest
data = json.loads(requests.get(link).text)

print(data["best_prices"][0])

