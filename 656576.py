import random

def generate_password(length, include_numbers=True, include_special_chars=True):
    """
    Генерирует случайный пароль заданной длины.
    
    Args:
        length (int): Длина пароля.
        include_numbers (bool): Включать ли в пароль цифры.
        include_special_chars (bool): Включать ли в пароль специальные символы.
    
