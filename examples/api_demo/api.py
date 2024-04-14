from typing import NoReturn, Union
import capra_micro_comm_py as ucomm

# This is an abstract class, you can implement your own manager
manager = ucomm.CommandManager() 


# This uses a simmilar formatting to the struct library
@manager.struct('if')
# You must inherit from BinaryData
class Foo(ucomm.BinaryData):
    def __init__(self, x:int=0, y:float=0): # Always leave to option for an empty constructor
        # Name the parameters here, this is the name they will get in c++
        super().__init__(x=x, y=y)
        
        # Optionnally hint the attributes and their type
        self.x:int
        self.y:float


# Use _ to indicate a sub-struct
@manager.struct('_ff')
class Bar(ucomm.BinaryData):
    def __init__(self, foo:Foo=Foo(), a:float=0, b:float=0):
        super().__init__(foo=foo, a=a, b=b)
        self.foo:Foo
        self.a:float
        self.b:float

@manager.command(ucomm.Byte, ucomm.Int)
def myCommand(arg:ucomm.Byte) -> Union[ucomm.Int, NoReturn]:
    # This will be called after having sent the encoded command
    # Returning a value here does nothing and is ignored
    pass

@myCommand.preCall
def preMyCommand(arg:ucomm.Byte) -> NoReturn:
    # This will be called just before sending the encoded command
    # You could use this to validate the parameter and raise an error if it is invalid
    pass

@myCommand.postCall
def postMyCommand(ret:ucomm.Int) -> NoReturn:
    # This will be called right after getting a response to the command
    pass



