import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_function_1():
    print("Thread 1: Trying to acquire lock A...")
    lock_a.acquire()
    time.sleep(1) # This gives the other thread time to acquire its lock
    print("Thread 1: Acquired lock A, now trying to acquire lock B...")
    lock_b.acquire()
    print("Thread 1: Acquired both locks.")
    lock_b.release()
    lock_a.release()

def thread_function_2():
    print("Thread 2: Trying to acquire lock B...")
    lock_b.acquire()
    time.sleep(1)
    print("Thread 2: Acquired lock B, now trying to acquire lock A...")
    lock_a.acquire()
    print("Thread 2: Acquired both locks.")
    lock_a.release()
    lock_b.release()

thread1 = threading.Thread(target=thread_function_1)
thread2 = threading.Thread(target=thread_function_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program finished.") # This line won't be reached in the deadlock scenario