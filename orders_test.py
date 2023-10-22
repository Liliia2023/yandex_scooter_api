 # Лилия Федотова, группа 09 Земля — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Функция для позитивной проверки
def positive_assert(track_number):
    response = sender_stand_request.get_order_number(track_number)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

# Тест №1
def test_get_order_number_success_response():
    positive_assert(sender_stand_request.track_number)
