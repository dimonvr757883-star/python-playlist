class Track:
    def __init__(self, executor, name, information):
        self.executor = executor
        self.name = name
        self.information = information

    def to_dict(self):
        return {
            "name": self.name,
            "executor": self.executor,
            "information": self.information
        }