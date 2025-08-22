"""Semaphore
A Semaphore is a more advanced lock. It allows a specific number of threads to access a resource simultaneously, not just one. 
It's like a counter for access permits. 
You initialize it with a number of available permits. A thread acquire()s a permit to enter, and release()s a permit when it's done.
In our example, we'll use a semaphore to limit the number of threads that can access a resource to 3 at a time."""

import threading
import time

# Semaphore initialized to allow 3 threads at a time
semaphore = threading.Semaphore(3)

def limited_access_worker(worker_id):
    print(f"Worker {worker_id} waiting for semaphore permit.")
    semaphore.acquire()  # Decrement the semaphore counter (wait if 0)
    try:
        print(f"Worker {worker_id} acquired permit and is working.")
        time.sleep(2)  # Simulate some work
    finally:
        print(f"Worker {worker_id} releasing permit.")
        semaphore.release() # Increment the semaphore counter

# Create 5 threads
threads = [threading.Thread(target=limited_access_worker, args=(i,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()