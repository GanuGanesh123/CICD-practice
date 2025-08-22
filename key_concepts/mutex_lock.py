import threading
import time

shared_counter = 0
lock = threading.Lock()

def increment_with_lock():
    global shared_counter
    for _ in range(1000000):
        lock.acquire()  # Acquire the lock before accessing shared data
        try:
            shared_counter += 1
        finally:
            lock.release()  # Always release the lock, even if an error occurs

def increment_without_lock():
    global shared_counter
    for _ in range(1000000):
        shared_counter += 1

# Demonstrate with a lock (correct result)
shared_counter = 0
thread1 = threading.Thread(target=increment_with_lock)
thread2 = threading.Thread(target=increment_with_lock)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"Final counter with lock: {shared_counter}") # Output will be 2000000

# Demonstrate without a lock (incorrect result)
shared_counter = 0
thread3 = threading.Thread(target=increment_without_lock)
thread4 = threading.Thread(target=increment_without_lock)
thread3.start()
thread4.start()
thread3.join()
thread4.join()
print(f"Final counter without lock: {shared_counter}") # Output will be less than 2000000