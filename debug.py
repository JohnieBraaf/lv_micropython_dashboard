import usys as sys
sys.path.append('') # See: https://github.com/micropython/micropython/issues/6419

# See: https://pymotw.com/2/sys/tracing.html

class Tracer():
    def mp_trace(self, frame, event, arg):
        co = frame.f_code
        func_name = co.co_name
        func_line_no = frame.f_lineno
        func_filename = co.co_filename
        print('[%s] [%s] %s:%s' % (event, func_name, func_filename, func_line_no))
        return mp_trace

    def start(self):
        sys.settrace(mp_trace)
