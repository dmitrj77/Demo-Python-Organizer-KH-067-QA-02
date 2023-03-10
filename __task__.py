import __app__
from utils import __data_utils__


def get_task_from_string(pattern):
    message = pattern.split(";")
    title = message[0]
    local_date_time = __app__.get_local_data_time(message[1])
    description = message[2]
    return Task(title, local_date_time, description)


class Task:

    def __init__(self, title, local_data_time, description):
        self.title = title
        self.local_data_time = local_data_time
        self.description = description

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_local_data_time(self, local_data_time):
        self.local_data_time = local_data_time

    def get_local_data(self):
        return self.local_data_time

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_string_for_file(self):
        data = __data_utils__.get_string_format(self.local_data_time)
        return str.format("%s;%s;%s" % (self.title, data, self.description))

    def to_string(self):
        data = __data_utils__.get_string_format(self.local_data_time)
        return str.format("Title: %s. Date: %s. Description: %s" % (self.title, data, self.description))
