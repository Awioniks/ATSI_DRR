#!/usr/bin/env python3

from server import Server
from config import Config_Queue, get_yaml_files
import argparse
import yaml


if __name__ == "__main__":

    # Get config values and initialize configurations for queues.

    config_list = []
    for config_file in get_yaml_files():
        with open(config_file) as conf_file:
            document = yaml.full_load(conf_file)
            config = Config_Queue(
                document["occurance_time"],
                document["link_rate"],
                document["packet_size"],
            )
            config_list.append(config)

    # Parse arguments here
    parser = argparse.ArgumentParser()
    parser.add_argument("defi", type=int, help="Deficit")
    args = parser.parse_args()
    assert 1000 <= args.defi <= 2000, "Deficit is between 1000 or 2000 boy"
    deficit = args.defi

    # Start simulation
    server = Server(config_list, deficit)

    try:
        server.start_simulation()
    except KeyboardInterrupt:
        print("\nBye\n")
