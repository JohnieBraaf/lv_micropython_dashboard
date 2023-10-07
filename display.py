import lvgl as lv
import rk043fn48h as lcd

class Display():
    def __init__(self):
        hres = 480
        vres = 272

        # Register display driver
        lcd.init(w=hres, h=vres)
        disp_drv = lv.disp_create(hres, vres)
        disp_drv.set_flush_cb(lcd.flush)
        buf1_1 = bytearray(hres * 50 * lv.color_t.__SIZE__)
        buf1_2 = bytearray(hres * 50 * lv.color_t.__SIZE__)
        disp_drv.set_draw_buffers(buf1_1, buf1_2, len(buf1_1), lv.DISP_RENDER_MODE.PARTIAL)

        # Register touch sensor
        indev_drv = lv.indev_create()
        indev_drv.set_type(lv.INDEV_TYPE.POINTER)
        indev_drv.set_read_cb(lcd.ts_read)
