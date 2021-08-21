import lvgl as lv

class ColorStyle(lv.style_t):
    def __init__(self, color):
        super().__init__()
        self.set_bg_opa(lv.OPA.COVER)
        self.set_bg_color(lv.color_hex3(color))
        self.set_bg_grad_color(lv.color_hex3(0xFFF))
        self.set_bg_grad_dir(lv.GRAD_DIR.VER)
        self.set_bg_main_stop(0)
        self.set_bg_grad_stop(128)

class ShadowStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_shadow_opa(lv.OPA.COVER)
        self.set_shadow_width(3)
        self.set_shadow_color(lv.color_hex3(0xAAA))
        self.set_shadow_ofs_x(5)
        self.set_shadow_ofs_y(3)
        self.set_shadow_spread(0)

# A square button with a shadow when not pressed
class ButtonStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_radius(lv.dpx(8))
        self.set_shadow_opa(lv.OPA.COVER)
        self.set_shadow_width(lv.dpx(10))
        self.set_shadow_color(lv.color_hex3(0xAAA))
        self.set_shadow_ofs_x(lv.dpx(10))
        self.set_shadow_ofs_y(lv.dpx(10))
        self.set_shadow_spread(0)

class ButtonPressedStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_shadow_ofs_x(lv.dpx(0))
        self.set_shadow_ofs_y(lv.dpx(0))