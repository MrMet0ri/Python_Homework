from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy S21", "+79234567890"),
    Smartphone("Xiaomi", "Mi 11", "+79345678901"),
    Smartphone("Huawei", "P40", "+79456789012"),
    Smartphone("OnePlus", "9 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")