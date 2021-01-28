from queue import Queue
from termcolor import colored
import time


class Server:
    def __init__(self, config_list, deficit):
        conf_A, conf_B, conf_C = config_list[:]
        self.queue_a = Queue(conf_A, "queue_A", deficit, "red")
        self.queue_b = Queue(conf_B, "queue_B", deficit, "green")
        self.queue_c = Queue(conf_C, "queue_C", deficit, "blue")

    def start_simulation(self):
        start = time.time()
        cycle_nr = 1
        while True:
            print(
                colored(cycle_nr, "magenta"),
                colored(".cycle nr ", "magenta"),
                round(self.check_time(start), 2),
                " sim_time",
            )
            self.queue_a.proccess_packets(self.check_time(start))
            self.queue_b.proccess_packets(self.check_time(start))
            self.queue_c.proccess_packets(self.check_time(start))
            cycle_nr += 1

    def check_time(self, start):
        return time.time() - start
