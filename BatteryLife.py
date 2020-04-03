import pywinusb.hid as hid
from time import sleep
import sys, signal
vendor_id = 0x1b1c
product_id = 0x0a14

devices = hid.HidDeviceFilter(vendor_id=vendor_id, product_id=product_id).get_devices()

def signal_handler(signal, frame):
    print("program terminated")
    sys.exit(0)

def sample_handler(data):
    life = data[2];
    if(life>127):
        print("Battery Life: {0} ".format(life-127), end = "\r")
    else:
        print("Battery Life: {0} ".format(life), end = "\r")

if devices:
    device = devices[2]
    print("Device Found")
    signal.signal(signal.SIGINT, signal_handler)
    device.open()
    device.set_raw_data_handler(sample_handler)
    while device.is_plugged():
        # just keep the device opened to receive events
        buffer = [0xC9, 0x64]
        device.send_output_report(buffer)
        sleep(10)    

else:
    print("no devices")