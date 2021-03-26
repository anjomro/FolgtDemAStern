
class Debug:
    """
    Class contains debug functionalities
    """
    active: bool = False

    @staticmethod
    def print(msg: str):
        """
        Simple debug print. Only prints if debug option is active
        :param msg: Message to print
        """
        if Debug.active:
            print(msg)

    @staticmethod
    def set_active():
        """
        Call at the beginning of the program to activate debug functionalities
        """
        Debug.active = True