import time


class TypingTime:
    @classmethod
    def timer_start(cls):
        cls.start = time.time()

    @classmethod
    def timer_end(cls):
        cls.end = time.time()

    @classmethod
    def interval(cls):
        return cls.end - cls.start
