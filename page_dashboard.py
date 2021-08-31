import machine
import lvgl as lv
#from lv_colors import lv_colors
from style import ColorStyle, ShadowStyle

class Page_Dashboard:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.test_events = []

        #self.page.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        #self.page.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)

        # create an arc
        self.arc = lv.arc(page)

        self.arc.set_size(200,200)
        self.arc.align(lv.ALIGN.TOP_LEFT, 0, 0)
        self.arc.set_rotation(180)
        self.arc.set_range(-40, 40)
        self.arc.set_end_angle(270)
        self.arc.set_bg_angles(180, 360)
        self.arc.set_start_angle(180)

        style = lv.style_t()
        #lv.style_copy(style, lv.style_plain)
        #style.line.color = lv.color_make(0,0,255) # Arc color
        #style.line.width = 8                      # Arc width
        #self.arc.set_style(lv.arc.STYLE.MAIN, style)   # Use the new style

        # counter button
        self.reset_btn = lv.btn(page)
        self.reset_btn.set_size(50,50)
        self.reset_btn.align(lv.ALIGN.TOP_RIGHT, 10, 10)
        self.reset_btn.add_event_cb(self.on_reset_btn, lv.EVENT.CLICKED, None)

        self.reset_label = lv.label(self.reset_btn)
        self.reset_label.set_text("Reset")
        self.reset_label.align(lv.ALIGN.CENTER, 0, 0)

        self.meter = lv.meter(page)
        self.meter.set_size(200, 200)
        self.meter.align(lv.ALIGN.TOP_RIGHT, -40, 15)

        self.scale_ticks = self.meter.add_scale()
        self.meter.set_scale_ticks(self.scale_ticks, 10, 2, 3, lv.palette_main(lv.PALETTE.GREY))
        self.meter.set_scale_range(self.scale_ticks, 0, 100, 100, 0)

        self.scale_major_ticks = self.meter.add_scale()
        self.meter.set_scale_major_ticks(self.scale_major_ticks, 42, 2, 10, lv.palette_main(lv.PALETTE.GREY), 2)

        indic = self.meter.add_needle_line(self.scale_ticks, 5, lv.palette_main(lv.PALETTE.BLUE), 10)
        self.meter.set_indicator_value(indic, 50)

        # slider
        #self.slider = lv.slider(page)
        #self.slider.set_width(lv.pct(80))
        #self.slider_label = lv.label(page)
        #self.slider.add_event_cb(self.on_slider_changed, lv.EVENT.VALUE_CHANGED, None)
        #self.on_slider_changed(None)

        # style selector
        #self.styles = [('Gray', ColorStyle(0xCCC)),
        #               ('Red', ColorStyle(0xF00)),
        #               ('Green',ColorStyle(0x0F0)),
        #               ('Blue', ColorStyle(0x00F))]

        #self.style_selector = lv.dropdown(page)
        #self.style_selector.add_style(ShadowStyle(), lv.PART.MAIN)
        #self.style_selector.align(lv.ALIGN.OUT_BOTTOM_LEFT, 0, 40)
        #self.style_selector.set_options('\n'.join(x[0] for x in self.styles))
        #self.style_selector.add_event_cb(self.on_style_selector_changed, lv.EVENT.VALUE_CHANGED, None)

        # counter button
        #self.counter_btn = lv.btn(page)
        #self.counter_btn.set_size(80,80)
        #self.counter_label = lv.label(self.counter_btn)
        #self.counter_label.set_text("Count")
        #self.counter_label.align(lv.ALIGN.CENTER, 0, 0)
        #self.counter_btn.add_event_cb(self.on_counter_btn, lv.EVENT.CLICKED, None)
        #self.counter = 0

    #def on_slider_changed(self, event):
    #    self.slider_label.set_text(str(self.slider.get_value()))

    def on_reset_btn(self, event):
        machine.reset()

    def on_style_selector_changed(self, event):
        selected = self.style_selector.get_selected()
        tabview = self.app.screen_main.tabview
        if hasattr(self, 'selected_style'): tabview.remove_style(self.selected_style, lv.PART.MAIN)
        self.selected_style = self.styles[selected][1]
        tabview.add_style(self.selected_style, lv.PART.MAIN)

    def on_counter_btn(self, event):
        self.counter += 1
        self.counter_label.set_text(str(self.counter))