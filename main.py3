import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі символи, крім цифр
    digits_only = re.sub(r"\D", "", phone_number)

    # Додаємо міжнародний код, якщо потрібно
    if digits_only.startswith("380"):
        normalized_number = "+" + digits_only
    elif digits_only.startswith("0"):
        normalized_number = "+38" + digits_only
    elif digits_only.startswith("38"):
        normalized_number = "+" + digits_only
    else:
        normalized_number = "+38" + digits_only  # fallback

    return normalized_number


# Список сирих номерів
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Обробка номерів
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Вивід результату
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)