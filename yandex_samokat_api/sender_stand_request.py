import configuration
import requests
import data
import create_user_test
#Функция создать заказ
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
response = post_create_order(data.body);
    #Получение трека
cod = response.json()
    #Получение номера трека
code = cod['track']
    #Номер в тип str
codes = str(code)
#Функция получить заказ по номеру
def get_order_receive():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER + codes)


