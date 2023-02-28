import os, platform
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            import jnxcx
        elif bit == '32bit':
            import Pro32
Run()
