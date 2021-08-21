import lvgl as lv
import rk043fn48h as lcd

class Display():
    def __init__(self):
        hres = 480
        vres = 272
        lcd.init(w=hres, h=vres)
        disp_buf1 = lv.disp_draw_buf_t()
        buf1_1 = bytearray(hres * 50 * lv.color_t.__SIZE__)
        buf1_2 = bytearray(hres * 50 * lv.color_t.__SIZE__)
        disp_buf1.init(buf1_1, buf1_2, len(buf1_1) // lv.color_t.__SIZE__)
        disp_drv = lv.disp_drv_t()
        disp_drv.init()
        disp_drv.draw_buf = disp_buf1
        disp_drv.flush_cb = lcd.flush
        disp_drv.hor_res = hres
        disp_drv.ver_res = vres
        disp_drv.register()

        # Register touch sensor
        indev_drv = lv.indev_drv_t()
        indev_drv.init()
        indev_drv.type = lv.INDEV_TYPE.POINTER
        indev_drv.read_cb = lcd.ts_read
        indev_drv.register()