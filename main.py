import functions
from data import *
from ciasses import *
from environs import Env
env = Env()

if __name__=='__main__':

    print ('это исполняемый файл')
    print(functions.get_double_number(100))
    print(my_dicy)

    myclass()