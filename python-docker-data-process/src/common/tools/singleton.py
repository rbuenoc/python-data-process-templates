class Singleton(object):
    instance = None

    def initialize(self):
        raise NotImplementedError('\'initialize\' method is not implemented on singleton.')

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
            cls.instance.initialize()

        return cls.instance
