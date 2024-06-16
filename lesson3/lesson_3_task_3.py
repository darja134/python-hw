from address import Address
from mailing import Mailing

from_address = Address(123456, "Moscow", "Gogolya st.", 15, 1)
to_address = Address(789012, "Kaliningrad", "Lenina st.", 16, 2)
track = "MS0001KL"
cost = 2500

mail = Mailing(to_address, from_address, cost, track)
mail.print_mail_info()
