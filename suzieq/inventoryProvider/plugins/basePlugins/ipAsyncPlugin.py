from abc import abstractmethod


class IpAsyncPlugin:
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

