import lvgl as lv
from lv_utils import event_loop
from display import Display
from theme import BaseTheme

from page_dashboard import Page_Dashboard
from page_controls import Page_Controls
from page_chart import Page_Chart
from page_test import Page_Test
import uasyncio

class Screen_Main(lv.obj):
    def __init__(self, app, *args, **kwds):
        self.app = app
        super().__init__(*args, **kwds)
        self.theme = BaseTheme()
        self.tabview = lv.tabview(self, lv.DIR.TOP, 20)
        self.page_test = Page_Test(self.app, self.tabview.add_tab("Test"))
        self.page_simple = Page_Dashboard(self.app, self.tabview.add_tab("Dashboard"))
        self.page_buttons = Page_Controls(self.app, self.tabview.add_tab("Controls"))
        self.page_chart = Page_Chart(self.app, self.tabview.add_tab("Chart"))

class AdvancedDemoApplication:
    def __init__(self):
        self.event_loop = event_loop()
        self.display = Display()

        self.screen_main = Screen_Main(self)
        lv.scr_load(self.screen_main)

import io

import time
async def heartbeat(console, repl):
    interval = 1000 # miliseconds
    last = time.ticks_ms()
    while True:
        #print('test')
        x = repl.buf.get_text()
        console.add_text(x)
        next = last + interval
        sleep = next - time.ticks_ms()
        if sleep > 0:
            print(sleep)
            await uasyncio.sleep_ms(sleep)
            last = next
        else:
            #print('ROBO: running late')
            last = time.ticks_ms()

from console import REPL
app = AdvancedDemoApplication()
repl = REPL(app.screen_main.page_test.console)
os.dupterm(repl, 2)

loop = uasyncio.get_event_loop()
loop.create_task(heartbeat(app.screen_main.page_test.console, repl))
loop.run_forever()
loop.close()