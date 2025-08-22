"""Producer-Consumer
The producer-consumer model is a classic concurrency problem. Producers create data and add it to a shared buffer, while consumers take data from the buffer and process it. This model is useful when the speed of production and consumption varies.

We'll use a queue.Queue from the standard library, which is a thread-safe way to implement a shared buffer. The Queue itself handles all the necessary locking, so you don't need to manually use locks for the queue operations.
"""

import threading
import time
import queue

shared_buffer = queue.Queue(maxsize=10)

def producer():
    for i in range(10):
        item = f"item_{i}"
        print(f"Producer producing {item}")
        shared_buffer.put(item)
        time.sleep(0.01)
    
    # After all items are produced, add a sentinel value
    shared_buffer.put(None)
    print("Producer has finished and sent a stop signal.")

def consumer():
    while True:
        item = shared_buffer.get()
        # Check if the received item is the sentinel value
        if item is None:
            print("Consumer received stop signal. Exiting...")
            shared_buffer.task_done()
            break  # Exit the loop
            
        print(f"___Consumer consuming {item}")
        shared_buffer.task_done()
        time.sleep(0.05)

# Create and start the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
print("Producer finished.")
consumer_thread.join()
print("Consumer finished.")
print("Program has finished.")