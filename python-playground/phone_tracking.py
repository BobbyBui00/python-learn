import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import time, random

def start_phone_tracer(target):
    print(f"[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace ...")
    p = phonenumbers.parse(target, None)
    print(f"[+] Location: {geocoder.description_for_number(p, "en")}")
    print(f"[+] Carrier: {carrier.name_for_number(p, "en")}")
    print(f"[+] Trace Complete")

start_phone_tracer("+1-514-583-6463")