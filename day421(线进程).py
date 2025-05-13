import multiprocessing
import threading
import os
import time
def dance(num):
    for i in range(num):
        print("dance")
        time.sleep(1)
def sing(num):
    for i in range(num):
        print("sing")
        time.sleep(1)

if __name__ == '__main__':

    # 进程,不共享全局变量
    # dance_process = multiprocessing.Process(target=dance,args=(5,))
    # sing_process = multiprocessing.Process(target=sing,args=(5,))
    # dance_process.start()
    # sing_process.start()
    # time.sleep(3)
    # # dance_process.terminate()
    # # sing_process.terminate() first way
    #
    # # os.kill(dance_process.pid,9)
    # # os.kill(sing_process.pid,9) second way
    #
    # # dance_process.kill()
    # # sing_process.kill() third way
    #
    # print(dance_process.pid)
    # print(sing_process.pid)
    #
    # 线程,共享全局变量
    # dance_process = threading.Thread(target=dance, args=(5,),daemon=True)
    # sing_process = threading.Thread(target=sing,args=(5,), daemon=True)
    # dance_process.start()
    # sing_process.start()
    # dance_process.join()
    # sing_process.join()
