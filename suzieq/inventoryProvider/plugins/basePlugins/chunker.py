from abc import abstractmethod

class Chunker:
    @abstractmethod
    def chunk(self,glob_inv,n_chunks,addl_parameters):
        ''' 
        Split the global inventory in <n_chunks> chunks 
        
        addl_parameters: this field is used to specify how to split the global inventory
        '''
        pass
