import lvgl as lv
from button import SymbolButton

class Page_Controls:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.member_name_cache = {}
        self.btn_event_count = {'Play': 0, 'Pause': 0}

        self.page.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.page.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.START)

        self.btn1 = SymbolButton(page, lv.SYMBOL.PLAY, "Play")
        self.btn1.set_size(80, 80)

        self.btn2 = SymbolButton(page, lv.SYMBOL.PAUSE, "Pause")
        self.btn2.set_size(80, 80)

        self.label = lv.label(page)
        self.label.add_flag(lv.obj.FLAG.IGNORE_LAYOUT)
        self.label.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)

        def button_cb(event, name):
            self.btn_event_count[name] += 1
            event_name = self.get_member_name(lv.EVENT, event.code)
            if all((not event_name.startswith(s)) for s in ['DRAW', 'GET', 'STYLE', 'REFR']):
                self.label.set_text('[%d] %s %s' % (self.btn_event_count[name], name, event_name))

        for btn, name in [(self.btn1, 'Play'), (self.btn2, 'Pause')]:
            btn.add_event_cb(lambda event, btn_name=name: button_cb(event, btn_name), lv.EVENT.ALL, None)

    def get_member_name(self, obj, value):
        try:
            return self.member_name_cache[id(obj)][id(value)]
        except KeyError:
            pass

        for member in dir(obj):
            if getattr(obj, member) == value:
                try:
                    self.member_name_cache[id(obj)][id(value)] = member
                except KeyError:
                    self.member_name_cache[id(obj)] = {id(value): member}
                return member