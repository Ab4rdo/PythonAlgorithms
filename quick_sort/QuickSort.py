

def sort(seq):
    """
    Implementation of basic quick sort algorithm
    :param seq: an integer list
    :return: new sorted integer list
    """
    index = partition(seq)

    return sort(partition(seq[:index])) + seq[index] + sort(partition(seq[index+1:]))


# Helping methods

def partition(seq):
    """
    Implementation of partition function
    :param seq:
    :return:
    """

    return 0

