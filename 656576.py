import random

def generate_password(length, include_numbers=True, include_special_chars=True):
    """
    Генерирует случайный пароль заданной длины.
    
    Args:
        length (int): Длина пароля.
        include_numbers (bool): Включать ли в пароль цифры.
        include_special_chars (bool): Включать ли в пароль специальные символы.
    
    Returns:
        str: Сгенерированный пароль.
    """
    
    # Определяем набор символов для пароля
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_numbers:
        characters += '0123456789'
    if include_special_chars:
        characters += '!@#$%^&*()_+~`|}{[]\:;?><,./-='
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Пример использования функции
password = generate_password(12, include_numbers=True, include_special_chars=True)
print(f'Сгенерированный пароль: {password}')
