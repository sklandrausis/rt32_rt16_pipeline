from enum import Enum
import casacore

class Status(Enum):
    not_selected = "not_selected"
    not_started = "not_started"
    started = "started"
    finished = "finished"


class Operation:
    def __init__(self):
        self.__status = Status.not_selected
        self.__name = ""
        self.__time_executed = 0

    def execute(self):
        pass

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def time_executed(self):
        return self.__time_executed

    @time_executed.setter
    def time_executed(self, time_executed):
        self.__time_executed = time_executed
