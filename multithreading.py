import time

import threading

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(i)

# Creating a thread
thread = threading.Thread(target=print_numbers)

# Starting the thread
thread.start()

# Waiting for the thread to finish
thread.join()

'''
for i in range(1, 6):
    time.sleep(1)
    print(i)
'''
