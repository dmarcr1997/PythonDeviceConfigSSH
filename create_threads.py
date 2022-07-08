import threading

def create_threads(list, function):

    threads = []

    for ip in list:
        th = threading.Thread(target=function, args=(ip,))
        th.start()
        threads.append(th)
    
    for th in threads:
        th.join()