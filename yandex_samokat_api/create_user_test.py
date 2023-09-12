#Гопеев Арсентий, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_order ():
    #Создать заказ
    order_response = sender_stand_request.post_create_order(data.body);
# Проверяется, что код ответа равен 201
    assert order_response.status_code == 201
def test_order_receive():
    order_receive = sender_stand_request.get_order_receive();
# Проверяется, что код ответа равен 200
    assert order_receive.status_code == 200




