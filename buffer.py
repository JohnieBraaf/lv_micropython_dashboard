#
# RingBuffer
#
# - size: number of bytes allocated to text
#
class RingBuffer:
    def __init__(self, size):
        self.size = size + 1
        self.data = bytearray(self.size)
        self.index_put = 0
        self.index_get = 0
        self.count = 0
    
    @micropython.native
    def any(self):
        if self.index_get != self.index_put:
            return True
        return False

    @micropython.native
    def put(self, value):
        next_index = (self.index_put + 1) % self.size
        
        if self.index_get != next_index: 
            self.data[self.index_put] = value
            self.index_put = next_index
            self.count += 1
            return value
        else:
            return 0x00  # buffer full
    
    @micropython.native
    def get(self):
        if self.any():
            value = self.data[self.index_get]
            self.index_get = (self.index_get + 1) % self.size
            self.count -= 1
            return value
        else:
            return 0x00  # buffer empty

#
# TextBuffer
#
# - size: number of bytes allocated to text
# - lines_max: maximum number of lines to keep in buffer (0xd new line delimited)
# - lines_trim: number of lines to trim if lines_max is reached
#
# Adds index_read to the ringbuffer, and dirty_read to flag if the reader is in sync
# get_text() resets the dirty_read flag, after which read_text() can be used for subsequent reads
#
class TextBuffer(RingBuffer):
    def __init__(self, size, lines_max, lines_trim):
        super().__init__(size)
        self.lines_max = lines_max
        self.lines_trim = lines_trim
        self.lines_count = 0
        self.index_read = 0
        self.dirty_read = False

    @micropython.native
    def put(self, value):
        if self.index_get == (self.index_put + 1) % self.size: # buffer full,
            self.get_line() # pop line from buffer

        super().put(value)

        if value == 0xd:
            self.lines_count += 1
            if self.lines_count > self.lines_max: # too many lines
                self.get_line(self.lines_trim) # pop number of lines from buffer

    @micropython.native
    def get_line(self, num=1, peek=False):
        old_index = self.index_get # save index
        old_count = self.count     # save count
        ret = ''
        for i in range(num):
            while self.any():
                c = self.get()
                if c == 0xd:
                    break
                ret += str(chr(c)) + str(hex(c))
        if peek:
            self.index_get = old_index # reset index
            self.count = old_count     # reset count
        else:
            self.lines_count -= num
        self.dirty_read = True
        return ret

    @micropython.native
    def get_text(self, peek=False):
        old_index = self.index_get # save index
        old_count = self.count     # save count
        ret = ''
        while self.any():
            ret += str(chr(self.get()))
        if peek:
            self.index_get = old_index # reset index
            self.count = old_count     # reset count
        self.dirty_read = False
        return ret

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
            return value
        else:
            return None  # buffer empty

    @micropython.native
    def read_text(self):
        ret = ''
        while self.any_read():
            ret += str(chr(self.read()))
        return ret