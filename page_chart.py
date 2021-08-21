import lvgl as lv
from chart import AnimatedChart
from style import ColorStyle, ShadowStyle

class Page_Chart:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.page.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.page.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.page.set_style_pad_all(10, lv.PART.MAIN)
        self.page.set_style_pad_gap(10, lv.PART.MAIN)
        self.chart = AnimatedChart(page, 100, 1000)
        self.chart.set_flex_grow(1)
        self.chart.set_height(lv.pct(100))
        self.series1 = self.chart.add_series(lv.color_hex(0xFF0000), self.chart.AXIS.PRIMARY_Y)
        self.chart.set_type(self.chart.TYPE.LINE)
        self.chart.set_style_line_width(3, lv.PART.ITEMS)
        self.chart.add_style(ColorStyle(0x055), lv.PART.ITEMS)
        self.chart.set_range(self.chart.AXIS.PRIMARY_Y, 0, 100)
        self.chart.set_point_count(10)
        self.chart.set_ext_y_array(self.series1, [10, 20, 30, 20, 10, 40, 50, 90, 95, 90])
        # self.chart.set_x_tick_texts("a\nb\nc\nd\ne", 2, lv.chart.AXIS.DRAW_LAST_TICK)
        # self.chart.set_x_tick_length(10, 5)
        # self.chart.set_y_tick_texts("1\n2\n3\n4\n5", 2, lv.chart.AXIS.DRAW_LAST_TICK)
        # self.chart.set_y_tick_length(10, 5)
        self.chart.set_div_line_count(5, 5)

        # Create a slider that controls the chart animation speed

        def on_slider_changed(event):
            self.chart.factor = self.slider.get_value()

        self.slider = lv.slider(page)
        self.slider.set_size(10, lv.pct(100))
        self.slider.set_range(10, 200)
        self.slider.set_value(self.chart.factor, 0)
        self.slider.add_event_cb(on_slider_changed, lv.EVENT.VALUE_CHANGED, None)