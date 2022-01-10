import platform
operSys = platform.system()

def check_system():
    system = None
    try:
        system = operSys
    except Exception as Error:
        return print(Error)
    return system