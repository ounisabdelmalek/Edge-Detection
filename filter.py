from abc import abstractmethod,ABC
import numpy as np
class Filter(ABC):
    """This abstract class ,you have to inhent if you want add any new filter"""
    @abstractmethod
    def run(self,image_path):
      """this methode to process the image"""