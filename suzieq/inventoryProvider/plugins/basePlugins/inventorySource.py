from abc import abstractmethod


class InventorySource:
   
    def __init__(self,input) -> None:
        ''' 
        1. Saves inside a data structure the raw content of <input>
        2. Calls <self.load_data>
        3. Calls <self.validate_data>
        
        '''
        pass

    @abstractmethod
    def load_data(self):
        ''' Store important informations from raw data '''
        pass

    @abstractmethod
    def validate_data(self):
        ''' Checks if the loaded data is valid or not '''
        pass

    @abstractmethod
    def run(self):
        ''' Function called from the inventory provider '''
        pass