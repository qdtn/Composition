

__author__ = 'quynhdo'
class Instance:
    '''
    Class representing an instance of the dataset
    '''
    def __init__(self, line, is_positive=True):
        '''
        line: a line in the textual data file: for example, American-j_battleship-n	battleship-n
        is_positive: is it a possitive instance or not
        '''
        line = line.lower()
        self.Adj=None
        self.Noun1=None
        self.Noun2=None
        self.label = None
        elements = line.split()

        if len(elements)==2:
            self.Noun2 = elements[1][0:len(elements[1])-2]
            temps = elements[0].split("_")
            if len(temps)==2:
                self.Adj = temps[0][0:len(temps[0])-2]
                self.Noun1 = temps[1][0:len(temps[1])-2]


        if self.Adj is not None and self.Noun1 is not None and self.Noun2 is not None:
            if is_positive:
                self.label = True
            else:
                self.label = False


def read_file(path, is_positive = True):
    '''
    read a data file, can be positive file or negative file
    :param path:
    :param is_positive:
    :return:
    '''
    data =[]
    f = open(path, "r")
    for line in f.readlines():
        line = line.strip()
        ins = Instance(line, is_positive)
        if ins.label is not None:
            data.append(ins)

    f.close()
    return data

def read_dataset(path_positive, path_negative):
    '''
    read the full dataset
    :param path_positive: path to positive file
    :param path_negative: path to negative file
    :return:
    '''
    data_pos = read_file(path_positive)
    data_neg = read_file(path_negative, False)
    data = data_pos + data_neg
    return data









