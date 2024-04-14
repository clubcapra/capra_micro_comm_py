import capra_micro_comm_py as ucomm
from . import api

def main():
    from .api import manager
    
    # Print the generated c++ code
    print(manager.generateAPI())
    
    # Call a command
    b:ucomm.Byte = api.myCommand(ucomm.Int(10))
    # This will do a few things:
    # 1- The preMyCommand function will be called
    # 2- The parameter will be encoded
    # 3- The data will be sent
    # 4.1- The myCommand function will be called
    # 4.2- If implemented and up to date with this api, the myCommand c++ code will be executed on the microcontroller
    # 5- The value returned from the c++ function will be encoded
    # 6- The data will be sent back to this program
    # 7- The data will be decoded
    # 8- The postMyCommand function will be called
    # 9- The value will be returned (b will be equal to the result from the c++ function)

if __name__ == '__main__':
    main()
