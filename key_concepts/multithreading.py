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

"""
Async: Single Thread/Single prcess (Parellelism)
-> FN (asycn Fn1, async Fn2, Fn3) CPU Scheduling
-> FN (async Fn1, Fn2, Fn3)



"""

alist = []
batch_size = 20
start_index =0
end_index = start_index + 20
@app.route(/)
def queue():
    while alist:
        alist.append({"a", 'b'})
        reqs_tosend = alist[start_index: end_index]
        request.post(url="addTwogen", reqs_tosend)
        start_index + = 20
        end_index _+= 20
        
# Database implementations
# status arrived
# get next_batch
# where status = arrived (sort in time)


