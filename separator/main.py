# May-07-2025
# main.py

from pathlib import Path
from utils.src.dir_support import read_directory_data
from basket_separation import basket_separation

"""
Images in the BASKET require PNG format and the RGB color space.
"""
dir_basket = Path.cwd() / 'BASKET'
list_basket_filepaths = read_directory_data(dir_basket)
n_basket_shapes = len(list_basket_filepaths)

print(f'\nThere are {n_basket_shapes} shapes in the BASKET folder.')
input_string = input('Please enter the desired number of parts: ')
number_of_parts = int(input_string)

basket_separation(dir_basket, number_of_parts)
