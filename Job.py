import datetime

class Job(object):

    def __init__(self,jobName, dueDate):
        self.name = jobName
        self.dueDate = dueDate


x = Job("jesse", datetime.date.today())