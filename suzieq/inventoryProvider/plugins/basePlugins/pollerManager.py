from abc import abstractmethod

class InventoryProvider:
    @abstractmethod
    def apiSubmit():
        pass

    @abstractmethod
    def run(inventory_chunks):
        pass
