import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from number import phn_number


print(f"You entered {phn_number}")
# using geocoder, finds location and ISP
ch_number = phonenumbers.parse(phn_number, None)
print("You are located in")
print(geocoder.description_for_number(ch_number, "en"))

print("Your service provider is")
ISP = phonenumbers.parse(phn_number, None)
print(carrier.name_for_number(ISP, "en"))
