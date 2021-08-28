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
            return None  # buffer full
    
    @micropython.native
    def get(self):
        if self.any():
            value = self.data[self.index_get]
            self.index_get = (self.index_get + 1) % self.size
            self.count -= 1
            return value
        else:
            return None  # buffer empty

    @micropython.native
    def get_text(self, peek=False):
        old_index = self.index_get # save index
        ret = ''
        while self.any():
            ret += str(chr(self.get()))
        if peek:
            self.index_get = old_index # reset index
        return ret