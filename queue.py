from time import sleep
from termcolor import colored
import math


class Queue:
    def __init__(self, conf, queue_id, deficit, color):
        self.color = color
        self.initial_deficit = deficit
        self.deficit = self.initial_deficit
        self.queue_id = queue_id
        self.occurance_time = conf.occurance_time
        self.link_rate = conf.link_rate
        self.packet_size = conf.packet_size
        self.last_time_queue_proccessing = 0
        self.packets_to_procceed = 0
        self.packets_in_queue = 1
        self.service_time = round(
            self.packet_size / (self.link_rate * 1000), 2)

    def proccess_packets(self, current_time):
        pkts_proccessed = 0
        if self.deficit == 0:
            self.deficit = self.initial_deficit

        if self.last_time_queue_proccessing:
            self.packets_in_queue = self.check_packets_in_queue(
                current_time) + self.packets_to_procceed

        self.last_time_queue_proccessing = current_time

        self.packets_to_procceed = 0
        if self.packets_in_queue:
            for _ in range(self.packets_in_queue):
                if not self.proccess_packet_success():
                    self.packets_to_procceed = self.packets_in_queue
                    - pkts_proccessed
                    return
                pkts_proccessed += 1
            self.deficit = 0
        else:
            print(colored(self.queue_id, self.color), " Empty queue")
            self.deficit = 0
            return

    def check_packets_in_queue(self, current_time):
        return math.floor(
            (current_time - self.last_time_queue_proccessing)
            / self.occurance_time
        )

    def proccess_packet_success(self):
        print(
            colored(self.queue_id, self.color),
            "Start Proccessing Packet"
        )
        if self.deficit < self.packet_size:
            print(
                colored(self.queue_id, self.color),
                " Deficit is not enough, Packet Size: ",
                self.packet_size,
                " Deficit: ",
                self.deficit,
            )
            self.deficit = self.deficit + self.initial_deficit
            print(
                colored(self.queue_id, self.color),
                " New Deficit: ",
                self.deficit
            )
            return False
        else:
            self.deficit = self.deficit - self.packet_size
        sleep(self.service_time)
        print(
            colored(self.queue_id, self.color),
            "Finished Proccessing Packet"
        )
        return True
