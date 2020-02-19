import pywinusb.hid as hid
from time import sleep

vendor_id = 0x1b1c
product_id = 0x0a14

devices = hid.HidDeviceFilter(vendor_id=vendor_id, product_id=product_id).get_devices()

if devices:
    device = devices[1]
    print("Found Device")
    num = int(input("Sidetone Level: "))
    while(num>255 | num<200):
        num = int(input("Sidetone Level: "))
    buffer = [0x0]*64
    buffer[0:16] = [0xFF, 0x0B, 0, 0xFF, 0x04, 0x0E, 0xFF, 0x05, 0x01, 0x04, 0x00, num, 0, 0, 0, 0]
    print(len(buffer))
    try:
        device.open()
        device.send_feature_report(buffer)
    finally:
        device.close()   

else:
    print("no devices")