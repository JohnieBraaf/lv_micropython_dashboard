import lvgl as lv
from style import ColorStyle, ShadowStyle

class Page_Dashboard:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.test_events = []

        self.page.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        self.page.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)

        # slider
        self.slider = lv.slider(page)
        self.slider.set_width(lv.pct(80))
        self.slider_label = lv.label(page)
        self.slider.add_event_cb(self.on_slider_changed, lv.EVENT.VALUE_CHANGED, None)
        self.on_slider_changed(None)

        # style selector
        self.styles = [('Gray', ColorStyle(0xCCC)),
                       ('Red', ColorStyle(0xF00)),
                       ('Green',ColorStyle(0x0F0)),
                       ('Blue', ColorStyle(0x00F))]

        self.style_selector = lv.dropdown(page)
        self.style_selector.add_style(ShadowStyle(), lv.PART.MAIN)
        self.style_selector.align(lv.ALIGN.OUT_BOTTOM_LEFT, 0, 40)
        self.style_selector.set_options('\n'.join(x[0] for x in self.styles))
        self.style_selector.add_event_cb(self.on_style_selector_changed, lv.EVENT.VALUE_CHANGED, None)

        # counter button
        self.counter_btn = lv.btn(page)
        self.counter_btn.set_size(80,80)
        self.counter_label = lv.label(self.counter_btn)
        self.counter_label.set_text("Count")
        self.counter_label.align(lv.ALIGN.CENTER, 0, 0)
        self.counter_btn.add_event_cb(self.on_counter_btn, lv.EVENT.CLICKED, None)
        self.counter = 0

    def on_slider_changed(self, event):
        self.slider_label.set_text(str(self.slider.get_value()))

    def on_style_selector_changed(self, event):
        selected = self.style_selector.get_selected()
        tabview = self.app.screen_main.tabview
        if hasattr(self, 'selected_style'): tabview.remove_style(self.selected_style, lv.PART.MAIN)
        self.selected_style = self.styles[selected][1]
        tabview.add_style(self.selected_style, lv.PART.MAIN)

    def on_counter_btn(self, event):
        self.counter += 1
        self.counter_label.set_text(str(self.counter))