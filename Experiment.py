from Composition import get_composition_rep_concat, get_composition_rep_sum, get_composition_rep_sum_weight
from Reader import read_dataset
from WEDict import WEDict

__author__ = 'quynhdo'

def create_csv_file(data, output, composition_func, we_dict):
    f = open(output, "w")

    idx=0

    for instance in data:


        representation_AN = composition_func(instance.Adj, instance.Noun1, we_dict)
        representation_N = we_dict.getWE(instance.Noun2)

        if idx==0:

            for i in range(representation_AN.shape[0]):
                f.write("an" + str(i))
                f.write(",")
            for i in range(representation_N.shape[0]):
                f.write("n" + str(i))
                f.write(",")
            f.write("class\n")
        #write to file
        for i in range(representation_AN.shape[0]):
            f.write(str(representation_AN[i]))
            f.write(",")
        for i in range(representation_N.shape[0]):
            f.write(str(representation_N[i]))
            f.write(",")
        f.write(str(instance.label))
        f.write("\n")
        idx+=1
    f.close()


if __name__ == "__main__":
    we_dict = WEDict("sg32.txt")

    data = read_dataset("positive_instances.txt", "negative_instances.txt")

    create_csv_file(data, "ann_weight.csv", get_composition_rep_sum_weight, we_dict )
