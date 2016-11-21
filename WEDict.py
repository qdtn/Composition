__author__ = 'quynhdo'

import numpy as np
import re

class WEDict:
    '''
    This class is used to read a word embedding file
    Each line contain a word embedding in the form of "word embedding_value1 embedding_value2 ..."
    '''

    def __init__(self, full_dict_path=None):
        '''

        :param full_dict_path: path to the we file
        :return:
        '''
        f = open(full_dict_path, "r")
        self.full_dict = {}
        self.we_size = -1
        for l in f.readlines(): # read the full dictionary
            l = l.strip()
            tmps = re.split('\s+', l)
            if len(tmps) > 1:
                we = []
                if self.we_size == -1:
                    self.we_size = len(tmps)-1
                for i in range(1, len(tmps)):
                    we.append(float(tmps[i].strip()))

                self.full_dict[tmps[0]]= np.asarray(we)

        f.close()




    def getWE(self, w):
        if w in self.full_dict.keys():
            return  self.full_dict[w]
        else:
            return np.zeros(self.we_size)



