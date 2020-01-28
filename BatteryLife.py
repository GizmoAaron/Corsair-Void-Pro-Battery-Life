import pywinusb.hid as hid
from time import sleep

vendor_id = 0x1b1c
product_id = 0x0a14

devices = hid.HidDeviceFilter(vendor_id=vendor_id, product_id=product_id).get_devices()

def sample_handler(data):
    print("Battery Life: {0}".format(data[2]))

if devices:
    device = devices[0]
    print("success")

    device.open()
    device.set_raw_data_handler(sample_handler)
    while device.is_plugged():
        # just keep the device opened to receive events
        buffer = [0xC9, 0x64]
        device.send_output_report(buffer)
        sleep(10)    

else:
    print("no devices")