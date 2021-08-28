import io
import lvgl as lv

from buffer import RingBuffer
class Textbuffer(RingBuffer):
    def __init__(self, size):
        super().__init__(size)
        self.index_read = 0

    @micropython.native
    def any_read(self):
        if self.index_read != self.index_put:
            return True
        return False

    @micropython.native
    def read(self):
        if self.any_read():
            value = self.data[self.index_read]
            self.index_read = (self.index_read + 1) % self.size
            self.count -= 1
            return value
        else:
            return None  # buffer empty

    @micropython.native
    def read_text(self):
        ret = ''
        while self.any_read():
            ret += str(chr(self.read()))
        return ret


class REPL(io.IOBase):
    def __init__(self, console):
        self.console = console
        self.buf = Textbuffer(30)
        self.ring = RingBuffer(10)

    def readinto(self, buf, nbytes=0):
        return None

    def write(self, buf):
        i = 0
        line = ''
        while i < len(buf):
            c = buf[i]
            if c == 0x1b: # remove escape chars
                i += 1
                while chr(buf[i]) in '[;0123456789':
                    i += 1
                c = buf[i]
                if c != 0x4b and c != 0x4:
                    self.console.add_text(hex(c))
            else:
                if c == 0x8: # backspace
                    self.console.del_char()
                elif c != 0xa: # if not white line collect output
                    line += str(chr(c))
                    #self.buf.add(chr(c))
                    self.buf.put(c)
                    self.ring.put(c)

            i += 1

        #self.console.add_text(line)

        #.readjust_scroll(1)

        #if len(buf) == 1:
        #    self.buf.append(buf[0])
        #    if buf[0] == 56: # Backspace
        #        self.console.add_text('jaaa')
        #        #print(buf[0])
        #    elif buf[0] == 0x44: # Escape character
        #        self.console.add_text('jypppp')
        #    elif buf[0] == 8: # Escape character
        #        self.console.add_text('jopppp')

        #    else:
        #        self.console.add_text('nee')
        #        self.console.add_text(buf)
        #        #print(buf[0])
        #else:
        #    self.console.add_text(buf)

        #self.console.add_text(self.buf.get_text())
        self.console.add_text(self.buf.read_text())
        #self.console.add_text(self.ring.get_text())

        return len(buf)

class Console(lv.textarea):
    def __init__(self, parent):
        super().__init__(parent)
        self.set_cursor_click_pos(False)