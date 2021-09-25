import pandas as pd
import os
import sys
from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import requests

root = Path('./')
input_path = root/'inputs'

class map:

    def __init__(self, file=input_path/'input1.txt'):
        self.info = self.__file_to_dict_info(file)
        self.tiles = self.__file_to_tiles(self.info['map'])
        self.constraints = self.info["constraints"]
        self.offices =  self.__get_offices(self.tiles)
    
    def __file_to_tiles(self, file):
        '''
        returns map (matrix form)
        each cell is a dict: score (int), type (str), walkable 
        '''
        return np.array([1,2])
    

    def __file_to_dict_info(self, file):
        return None
    
    def __get_offices(self, tiles):
        '''
        returns a list of office coordinates (tuples ())
        '''
        return [(1,1)]
    
    def get_cell(self, x, y):
        return x, y
    
    def get_score(self, x, y):
        return None
    
    def get_type(self, x, y):
        return None



# class build:



    