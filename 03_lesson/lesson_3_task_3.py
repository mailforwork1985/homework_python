from address import Address
from mailing import Mailing


to_addr = Address("00000", "Санкт-Петербург", "Невский проспект", "1", "2")
from_addr = Address("11111", "Москва", "Тверская улица", "2", "3")
mailing_item = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=100,
    track="RU1111111111"
)
track = mailing_item.track
cost = mailing_item.cost

f_adr = mailing_item.from_address
t_adr = mailing_item.to_address

print(
    f"Отправление {track} из {f_adr.index}, {f_adr.city}, {f_adr.street}, "
    f"{f_adr.house} - {f_adr.apartment} "
    f"в {t_adr.index}, {t_adr.city}, {t_adr.street}, "
    f"{t_adr.house} - {t_adr.apartment}. "
    f"Стоимость {cost} рублей."
)
