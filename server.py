from queue import Queue
import time


class Server:
    def __init__(self, config_list, deficit):
        conf_A, conf_B, conf_C = config_list[:]
        self.queue_a = Queue(conf_A, "queue_A")
        self.queue_b = Queue(conf_B, "queue_B")
        self.queue_c = Queue(conf_C, "queue_C")
        self.initial_deficit = deficit

    def start_simulation(self):
        start = time.time()
        cycle_nr = 1
        while True:
            current = time.time()
            sim_time = current - start
            print(cycle_nr, ". cycle nr ", round(sim_time, 2), " sim_time")
            self.queue_a.proccess_packets(sim_time)
            self.queue_b.proccess_packets(sim_time)
            self.queue_c.proccess_packets(sim_time)
            cycle_nr += 1
