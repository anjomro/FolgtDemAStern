
class Debug:
    active:bool = False

    @staticmethod
    def print(msg:str):
        if Debug.active:
            print(msg)

    @staticmethod
    def set_active():
        Debug.active = True