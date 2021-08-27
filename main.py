import lvgl as lv
from lv_utils import event_loop
from display import Display
from theme import BaseTheme

from page_dashboard import Page_Dashboard
from page_controls import Page_Controls
from page_chart import Page_Chart
from page_test import Page_Test

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

from machine import UART
class UARTListener(UART):
    def write(self, buf):
        #print('write')
        super().write(buf)

import io
class Console(io.IOBase):
    def __init__(self, console):
        self.console = console
        self.uart = UARTListener(1, 115200, timeout=100, timeout_char=100)
        self.buf = bytearray(1024)

    def write(self, buf):
        #print('write')
        #self.uart.write(buf)
        #i = 0
        #x = None
        self.x = 0
        if len(buf) == 1:
            self.buf.append(buf[0])
            if buf[0] == 56: # Backspace
                self.console.add_text('jaaa')
                #print(buf[0])
            elif buf[0] == 0x44: # Escape character
                self.console.add_text('jypppp')
            elif buf[0] == 8: # Escape character
                self.console.add_text('jopppp')

            else:
                self.console.add_text('nee')
                self.console.add_text(buf)
                #print(buf[0])
        else:
            self.console.add_text(buf)

        #print(str(x))
        #return None



        #print(len(buf))

    def readinto(self, buf, nbytes=0):
        #print('read')
        #super.readinto(buf, nbytes)
        return None

app = AdvancedDemoApplication()
c = Console(app.screen_main.page_test.console)
os.dupterm(c, 2)


#os.dupterm(None, 1)
#uart = UARTListener(1, 115200, timeout=100, timeout_char=100)
#os.dupterm(UARTListener(1, 115200), 1)
#console = os.dupterm(None)

def setup():
    os.dupterm(None, 1)
    uart = UARTListener(1, 115200, timeout=100, timeout_char=100)
    os.dupterm(uart, 1)