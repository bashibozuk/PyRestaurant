import threading
import time


class Restaurant:
    def __init__(self):
        self.cashiers = 5
        self.customers = 10
        self.semaphore = threading.Semaphore(self.cashiers)

    def work(self):
        for i in range(self.customers):
            t = self.get_customer_thread()
            t.start()

        time.sleep(5)
        print("")

    def get_customer_thread(self):
        t = CustomerThread()
        t.set_semaphore(self.semaphore)
        t.set_restaurant(self)
        t.daemon = True
        return t

    def on_new_customer(self):
        t = self.get_customer_thread()
        self.customers += 1
        t.start()

    def on_customer_leave(self):
        self.customers -= 1


class CustomerThread(threading.Thread):
    def set_semaphore(self, semaphore: threading.Semaphore):
        self.semaphore = semaphore

    def set_restaurant(self, restaurant: Restaurant):
        self.restaurant = restaurant

    def run(self):
        print("Waiting for cashier")
        self.semaphore.acquire()
        time.sleep(5)
        print("Leaving restaurant - " + self.getName())
        self.semaphore.release()
        self.restaurant.on_customer_leave()
