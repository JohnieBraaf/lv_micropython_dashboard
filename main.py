import lvgl as lv
from lv_utils import event_loop
from display import Display
from theme import BaseTheme

from page_dashboard import Page_Dashboard
from page_controls import Page_Controls
from page_chart import Page_Chart

class Screen_Main(lv.obj):
    def __init__(self, app, *args, **kwds):
        self.app = app
        super().__init__(*args, **kwds)
        self.theme = BaseTheme()
        self.tabview = lv.tabview(self, lv.DIR.TOP, 20)
        self.page_simple = Page_Dashboard(self.app, self.tabview.add_tab("Dashboard"))
        self.page_buttons = Page_Controls(self.app, self.tabview.add_tab("Controls"))
        self.page_chart = Page_Chart(self.app, self.tabview.add_tab("Chart"))

class AdvancedDemoApplication:
    def __init__(self):
        self.event_loop = event_loop()
        self.display = Display()

        self.screen_main = Screen_Main(self)
        lv.scr_load(self.screen_main)

app = AdvancedDemoApplication()