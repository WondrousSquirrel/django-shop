from .cart import Cart


def cart(request):
    # возвращаем словарь, который будет отображаться во всех шаблонах
    return {'cart': Cart(request)}
