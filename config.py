from dataclasses import dataclass
import os
import fnmatch


@dataclass
class Config_Queue:
    occurance_time: int
    link_rate: int
    packet_size: int


def get_yaml_files():
    file_format = "{}/{}"
    for config_file in os.listdir('./configs'):
        if fnmatch.fnmatch(config_file, '*.yaml'):
            yield file_format.format('./configs', config_file)
