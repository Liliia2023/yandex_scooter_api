import configuration
import requests
import data


# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


response = post_new_order(data.order_body)

# Сохранение трекингового номера заказа

track_number = response.json()["track"]

# print(track_number)


# Получение заказа по трекинговому номеру
def get_order_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track})


response = get_order_number(track_number)

order = response.json()["order"]
order_id = order["id"]
# print(order_id)

