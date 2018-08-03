# -*- coding: utf-8 -*-

import os
"""
I dont know if this is significantly necessary or not but I do it for my own comfort
Usual used variables is stored here. Not absolutely CONSTANT though
"""

dir = os.path.abspath(__file__).split("/")
ROOT_DIR = "/".join(dir[0:len(dir)-2])
# print(ROOT_DIR)

WORD_BEGIN = "B_W"
WORD_INSIDE = "I_W"
punctuations_and_symbols = ['.', ',', '…', ';', ':', '/', '"', '\'', '?', '>', '<', ']', '[', '(', ')', '*', '&',
                            '!', 'oOo', '”', '“', '-', '+', '=', '--------']


# DATASET_SUPPORT = {'vi': self.reader_tieng_viet, 'en': reader_tieng_anh}
# DATASET_SUPPORT = ['vi', 'en']

# “/“ International_Muay/Np (/( Muay/Np quốc_tế/N )/) ”/”