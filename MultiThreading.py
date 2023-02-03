import threading
import time

# Credits: https://www.youtube.com/watch?v=e05Hkz-W_aQ&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=3

# Part-1
# def hello():
#     print("Hello World")

# t = threading.Thread(target=hello)
# t.start()




# Part-2
# def function1():
#     for i in range(10):
#         print("function1")

# def function2():
#     for i in range(10):
#         print("function2")

# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)

# t1.start()
# t2.start()




# Part-3
# def function1():
#     for i in range(10):
#         print("function1")
#         time.sleep(2)

# t1 = threading.Thread(target=function1)
# t1.start()

#Dont go to next line until t1 is finished
# t1.join()
# time.sleep(3)
# print("Done")




# Part-4
# Syncronization of Threads
# import time
# x = 8192
# def double():
#     global x
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the max value!")

# def halve():
#     global x
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the min value!")

# t1 = threading.Thread(target=double)
# t2 = threading.Thread(target=halve)

# t1.start()
# t2.start()

# Here we can see that both threads are running at the same time and competing each other, and they use the same variable x. So, we need to make sure that they are not using the same variable at the same time. So, we need to use Locks to Lock the resources.
# import time
# x = 8192
# Lock = threading.Lock()
# def double():
#     global x, Lock
#     Lock.acquire()
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the max value!")
#     Lock.release()

# def halve():
#     global x, Lock
#     Lock.acquire()
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the min value!")
#     Lock.release()

# t1 = threading.Thread(target=double)
# t2 = threading.Thread(target=halve)

# t1.start()
# t2.start()



# Part-5
# import time
# # Semaphore is used to limit the number of threads that can access a resource at the same time.
# semaphore = threading.BoundedSemaphore(value=2)

# def accessResource(threadNumber):
#     print("Thread {} is trying to access the resource".format(threadNumber))
#     print("Accessing the resource")
#     semaphore.acquire()
#     print(f"Thread {threadNumber} is using the resource")
#     time.sleep(10)
#     print("Releasing the resource")
#     semaphore.release()

# for threadNumber in range(1, 6):
#     thread = threading.Thread(target=accessResource, args=(threadNumber,))
#     thread.start()




# Part-6
# import time

# # Event is used to make functions get triggered when a certain event happens.

# event = threading.Event()

# def wait():
#     print("Waiting for the event trigger")
#     event.wait()
#     print("Event is triggered")

# t1 = threading.Thread(target=wait)
# t1.start()

# x = input("Press any key to trigger the event")
# event.set()



# Part-7

# Daemon Threads are threads that run in the background and does not block the main thread from exiting and continues to run in background. They are used for logging, monitoring, etc.
# import module
# from threading import *
# import time

# def thread_1():				
#     for i in range(5):
#         print('this is non-daemon thread')
#         time.sleep(2)

# T = Thread(target=thread_1)
# T.start()	

# # main thread stop execution till 5 sec.
# time.sleep(5)				
# print('main Thread execution')



# Part-8

# # import modules
# from threading import *
# import time

# # creating a function
# def thread_1():					
#     for i in range(5):
#         print('this is thread T')
#         time.sleep(3)

# # creating a thread
# T = Thread(target = thread_1)

# # change T to daemon
# T.setDaemon(True)				

# # starting of Thread T
# T.start()						
# time.sleep(5)
# print('this is Main Thread')
