from abc import abstractmethod
from threading import Semaphore


class InventorySource:
   
    def __init__(self,input) -> None:
        ''' 
        1. Saves inside a data structure the raw content of <input>
        2. Calls <self.load_data>
        3. Calls <self.validate_data>
        
        '''
        self._sem : Semaphore
        pass

    @abstractmethod
    def load_data(self):
        ''' Store important informations from raw data '''
        pass

    @abstractmethod
    def validate_data(self):
        ''' Checks if the loaded data is valid or not '''
        pass

    
    def get_inventory(self):
        '''
        - Acquire semaphore
        - Copy inventory
        - Release semaphore
        - Return inventory
        '''
        pass

    def set_inventory(self):
        '''
        - Acquire semaphore
        - Update inventory
        - Release semaphore
        '''
        pass

    @abstractmethod
    def run(self):
        ''' Function called from the inventory provider that gathers data from the source'''
        while True:
            # get_data

            if run_once:
                break

            sleep(period)
        
