from urandom import getrandbits, seed
from utime import ticks_us
from uasyncio import sleep, create_task, Loop, CancelledError
import lv_utils
import lvgl as lv

class MsgBox(lv.win):

    def drag_event_handler(self, e):
        self.move_foreground()
        indev = lv.indev_get_act()
        indev.get_vect(self.vect)
        x = self.get_x() + self.vect.x
        y = self.get_y() + self.vect.y
        self.set_pos(x, y)

    def __init__(self, parent):
        super().__init__(parent, 20)
        self.vect = lv.point_t()

        self.set_size(100,80)
        self.add_title("Pop")
        msg_box_close_btn = self.add_btn(lv.SYMBOL.CLOSE, 20)
        msg_box_close_btn.add_event(lambda e: self.close_msg_box(), lv.EVENT.RELEASED, None)

        header = self.get_header()
        header.set_style_bg_color(lv.color_hex3(0xFEE), lv.PART.MAIN)

        content = self.get_content()
        content.set_style_bg_color(lv.color_hex3(0xFFF), lv.PART.MAIN)

        self.set_style_border_width(4, lv.PART.MAIN)
        self.set_style_border_color(lv.color_hex3(0xF88), lv.PART.MAIN)
        self.set_style_shadow_color(lv.color_hex3(0x000), lv.PART.MAIN)
        self.set_style_shadow_opa(50, lv.PART.MAIN)
        self.set_style_shadow_width(20, lv.PART.MAIN)
        self.set_style_shadow_ofs_x(10, lv.PART.MAIN)
        self.set_style_shadow_ofs_y(10, lv.PART.MAIN)
        self.set_style_shadow_spread(0, lv.PART.MAIN)
        self.set_style_radius(10, lv.PART.MAIN)

        self.label = lv.label(content)

        for element in [content, header]:
            element.add_event(self.drag_event_handler, lv.EVENT.PRESSING, None)

        self.opened = True;

    def is_open(self):
        return self.opened

    def close_msg_box(self):
        if self.is_open():
            self.anim = lv.anim_t()
            self.anim.init()
            self.anim.set_var(self)
            self.anim.set_time(500)
            self.anim.set_values(lv.OPA.COVER,lv.OPA.TRANSP)
            self.anim.set_custom_exec_cb(lambda obj, val:
                    self.set_style_opa(val, lv.PART.MAIN))
            self.anim.set_path_cb(lv.anim_t.path_ease_in)
            self.anim.set_ready_cb(lambda a: self.del_async())
            lv.anim_t.start(self.anim)
            self.opened = False

    def set_text(self, txt):

        # If the msg box is already closed, cancel the calling task
        if not self.is_open():
            raise CancelledError()

        self.label.set_text(txt)