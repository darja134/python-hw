from smartphone import Smartphone

phone_1 = Smartphone("Nokia", "3310", "+799999999999")
phone_2 = Smartphone("Siemens", "C60", "+790000000000")
phone_3 = Smartphone("Motorola", "C115", "+791111111111")
phone_4 = Smartphone("Sony Ericsson", "w610i", "+792222222222")
phone_5 = Smartphone("LG", "H410", "+793333333333")

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for i in range(0, len(catalog)):
    catalog[i].print_info()

#phone_error_1 = Smartphone("", "3310", "+799999999999")
#phone_error_2 = Smartphone("Nokia", "", "+799999999999")
#phone_error_3 = Smartphone("Nokia", "3310", "")
#phone_error_4 = Smartphone("", "", "")
phone_error_5 = Smartphone("Nokia", "3310", "+370999999999")
