from abc import abstractmethod


class InvProviderAsyncPlugin:
    @abstractmethod
    def run(self):
        """
        Function called to start the plugin
        """
        pass

    @abstractmethod
    def stop(self):
        '''
        Function called to stop the plugin
        '''

        pass
