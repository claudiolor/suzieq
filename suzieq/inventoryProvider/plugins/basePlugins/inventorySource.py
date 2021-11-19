from abc import abstractmethod
from copy import copy
from threading import Semaphore


class InventorySource:
    def __init__(self, input_data) -> None:
        """
        - Saves inside a data structure the raw content of <input>
        - Calls self.load
        - Calls self.validate_data
        """
        self._inv_semaphore = Semaphore()
        self._inventory = {}
        self._inv_is_set = False
        self._inv_is_set_sem = Semaphore()

        self.load(input_data)
        self.validate_data()

    @abstractmethod
    def load(self, input_data):
        """Store important informations from raw data"""
        pass

    @abstractmethod
    def validate_data(self):
        """Checks if the loaded data is valid or not"""
        pass

    def get_inventory(self, timeout: int = 10):
        """
        - Acquire semaphore
        - Copy inventory
        - Release semaphore
        - Return inventory
        """

        if timeout < 0:
            return None, ValueError(
                "timeout value must be positive, found {}".format(timeout)
                )

        ok = self._inv_is_set_sem.acquire(timeout=timeout)
        if not ok:
            return None, TimeoutError(
                "Unable to acquire the lock before the timeout expiration"
            )
        ok = self._inv_semaphore.acquire(timeout=timeout)
        if not ok:
            return None, TimeoutError(
                "Unable to acquire the lock before the timeout expiration"
            )

        if callable(getattr(self._inventory, "copy", None)):
            inventory_snapshot = self._inventory.copy()
        else:
            inventory_snapshot = copy(self._inventory)
        self._inv_semaphore.release()
        return inventory_snapshot

    def set_inventory(self, new_inventory):
        """
        - Acquire semaphore
        - Update inventory
        - Release semaphore
        """
        self._inv_semaphore.acquire()
        self._inventory = new_inventory
        if not self._inv_is_set:
            # the inventory has been set for the first time
            self._inv_is_set = True
            self._inv_is_set_sem.release()
        self._inv_semaphore.release()
