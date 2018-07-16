import os
import time

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
# TODO should define singleton here. Dictionary should only be loaded once
class Dictionary:
    def __init__(self):
        """ contains 13k words in this version
        """
        filepath = os.path.join(os.path.dirname(__file__), "Viet74K.txt")

        with open(filepath, "r") as f:
            self.words = {line.strip("\n").strip(" ") for line in f.readlines()}
            # self.words = [line.strip("\n").strip(" ") for line in f.readlines()]

        # with open(filepath, "rb") as f:
        #     self.words = pickle.load(f)

    def lookup(self, text):
        if text in self.words:
            return True

        return False

    def isInDict(self, word):
        if word in self.words:
            return True

        return False


# class VietDict(filepath):
#
#     filepath = os.path.join(os.path.dirname(__file__), "Viet74K.txt")
#
#     with open(filepath, "r") as f:
#         self.words = [line.strip("\n").strip(" ") for line in f.readlines()]


if __name__ == "__main__":
    start = time.time()
    vidic = Dictionary.Instance()
    end1 = time.time()
    vidic2 = Dictionary.Instance()
    end2 = time.time()

    print("Instantiate time: " + str(end1-start))
    print("Re-instantiate time: " + str(end2-end1))
    # print(vidic == vidic1)


