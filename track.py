class Track:
    def __init__(self, executor, name, information):
        self.executor = executor # автор
        self.name = name # название трека
        self.information = information # информация

    def to_dict(self):
        return {
            "name": self.name,
            "executor": self.executor,
            "information": self.information
        }