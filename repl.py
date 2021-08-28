import subprocess
subprocess.Popen("plink -serial \\.\COM7 -sercfg 115200,8,n,1,N", shell=False, stdin=subprocess.PIPE)

class REPL():
    def __init__(self):
        self.com_port = 'COM7'

