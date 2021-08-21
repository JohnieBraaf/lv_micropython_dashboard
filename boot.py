import machine
import pyb
import lvgl as lv

pyb.country('US') # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU
pyb.main('main.py') # main script to run after this one
pyb.usb_mode('VCP+MSC') # act as a serial and a storage device

lv.init() # LVGL needs to be initialized before it's used