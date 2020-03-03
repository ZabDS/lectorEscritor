import logging
import threading
import time

def Libro(lock):
    #logging.debug("Iniciando")
    
    while True:
        flag=lock.acquire(0)
        try:
            if flag:
                logging.debug("Accedió al libro")
                time.sleep(1)
            else:
                logging.debug("Intentó acceder al libro sin éxito")
                time.sleep(.2)
        finally:
            if flag:
                lock.release()
                break
    logging.debug("Terminado")

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()

Lector1 = threading.Thread(target=Libro,args=(lock,), name='Lector1')
Lector1.start()
Lector2 = threading.Thread(target=Libro,args=(lock,), name='Lector2')
Lector2.start()
Escritor1 = threading.Thread(target=Libro,args=(lock,), name='Escritor1') 
Escritor1.start()
Escritor2 = threading.Thread(target=Libro,args=(lock,), name='Escritor2') 
Escritor2.start()

#holder = threading.Thread(target=lock_holder,args=(lock,), name='LockHolder', daemon=True,)
#holder.start()

#worker = threading.Thread(target=worker, args=(lock,), name='Worker',)
#worker.start()