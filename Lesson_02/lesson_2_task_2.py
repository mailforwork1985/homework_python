def is_year_leap(year):
    return year % 4 == 0

check_year = int(input("Введите год для проверки: "))

result = is_year_leap(check_year)

print(f"год {check_year}: {result}")
