# import time
#
# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

import time
# from time import process_time as my_timer # time use by cpu to process
# from time import perf_counter as my_timer  # better means accurate time mesure
# from time import monotonic as my_timer  # same as perf_counter nut perf_counter is superior
from time import time as my_timer
import random

input('Press Enter to Start')

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press enter to stop')

end_time = my_timer()

print('Started at ' + time.strftime('%X', time.localtime(start_time)))
print('Ended at ' + time.strftime('%X', time.localtime(end_time)))

print(f'your Reaction time is {end_time - start_time} sec.')
