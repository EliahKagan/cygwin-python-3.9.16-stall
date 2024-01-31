import hashlib
import threading
import time
t1 = threading.Thread(target=lambda: print("hello"))
t2 = threading.Thread(target=lambda: print("goodbye"))
t1.start()
time.sleep(1)
print("in between")
t2.start()
t1.join()
t2.join()
