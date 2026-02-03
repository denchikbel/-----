import functions
from data import *
from ciasses import *
from environs import Env
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

if __name__=='__main__':

    print ('это исполняемый файл')
    print(functions.get_double_number(100))
    print(my_dicy)
    print(f'токен бота {bot_token}')

    myclass()