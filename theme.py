import lvgl as lv
from style import ButtonStyle, ButtonPressedStyle

class BaseTheme(lv.theme_t):

    def __init__(self):
        super().__init__()
        self.button_style = ButtonStyle()
        self.button_pressed_style = ButtonPressedStyle()

        # This theme is based on active theme (material)
        base_theme = lv.theme_get_from_obj(lv.scr_act())

        # This theme will be applied only after base theme is applied
        self.set_parent(base_theme)

        # Set the "apply" callback of this theme to our custom callback
        self.set_apply_cb(self.apply)

        # Activate this theme on default display
        lv.disp_get_default().set_theme(self)

    def apply(self, theme, obj):
        if obj.get_class() == lv.btn_class:
            obj.add_style(self.button_style, lv.PART.MAIN)
            obj.add_style(self.button_pressed_style, lv.PART.MAIN | lv.STATE.PRESSED)