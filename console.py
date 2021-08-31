import io
import lvgl as lv
from buffer import TextBuffer

class REPL(io.IOBase):
    def __init__(self, console):
        self.console = console
        self.buf = TextBuffer(1000, 15, 1)

    @micropython.native
    def readinto(self, buf, nbytes=0):
        return None

    @micropython.native
    def write(self, buf):
        i = 0
        while i < len(buf):
            c = buf[i]
            if c == 0x1b: # remove escape chars
                i += 1
                while chr(buf[i]) in '[;0123456789':
                    i += 1
                #c = buf[i]
                #if c != 0x4b and c != 0x4:
                #    self.console.add_text(hex(c))
            else:
                if c == 0x8: # backspace
                    self.console.del_char()
                elif c != 0xa: # normal character
                    self.buf.put(c)
            i += 1

        # print directly to console
        if self.buf.dirty_read:
            self.console.set_text(self.buf.get_text(True))
            self.buf.read_text() # flag all as read
        self.console.add_text(self.buf.read_text())

        return len(buf)
