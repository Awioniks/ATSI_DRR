from time import sleep
import math


class Queue:
    def __init__(self, conf, queue_id):
        self.queue_id = queue_id
        self.occurance_time = conf.occurance_time
        self.link_rate = conf.link_rate
        self.packet_size = conf.packet_size
        self.last_time_queue_proccessing = 0
        self.service_time = round(
            self.packet_size / (self.link_rate * 1000), 2)

    def proccess_packets(self, current_time):
        if self.last_time_queue_proccessing:
            packets_in_queue = self.check_packets_in_queue(current_time)
            if packets_in_queue:
                self.proccess_packet()
            else:
                print(self.queue_id, " Empty queue")
                return
        else:
            self.proccess_packet()
        self.last_time_queue_proccessing = current_time

    def check_packets_in_queue(self, current_time):
        return math.floor(
            (current_time - self.last_time_queue_proccessing)
            / self.occurance_time
        )

    def proccess_packet(self):
        print(self.queue_id, "Start Proccessing packets")
        sleep(self.service_time)
        print(self.queue_id, "Stop Proccessing packets")
