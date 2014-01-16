
class BaseCommand:
    def __init__(self, console):
        self.console = console
        
    def _callback(self, *args):
        """
        _callback() is the first function called when the command ballack is
        issued - this, in turn, calls callback(). This is used for hard-coded
        arguments, such as "<arg> help" to display the command's help menu.
        All other commands should override callback()/
        """
        if((args) and (args[0] in ["help","?"])):
            self.console.writeln(self.help())
        else:
            self.callback(*args)

    def callback(self, *args):
        raise NotImplementedError()

    @staticmethod
    def help():
        raise NotImplementedError()
