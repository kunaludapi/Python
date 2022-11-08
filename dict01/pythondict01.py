#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])

#print(switch["lynx"])

print("First test - .get()")
print(switch.get("lynx"))

print("second test -.get()")
print(switch.get("lynx", "The key is in another castle!"))

print("Third test - .get()")
print(switch.get("version"))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print("6th test - .pop()")
switch.pop("version")
print(switch.keys())
print(switch.values())

print("7th test - add a new value")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())

print("8th test - add a new value")
switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())
