def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


num = 2024
result = is_year_leap(num)
print(f"год {num}: {result}")
