
def sort(seq):
    """
    Implementation of selection sort algortihm
    :param seq: a integer list
    :return: new ascending sorted array
    """

    if not seq:
        raise ValueError('List is empty')

    i = 0
    length = len(seq)
    while i < length:
        mini = index_of_min(seq, i)
        temp = seq[i]
        seq[i] = seq[mini]
        seq[mini] = temp
        i += 1
    return seq

# Helping methods


def index_of_min(seq, i):
    """
    :param seq: a integer list
    :param i: most left-hand side index
    :return: index of the smallest element in seq starting form i index
    """
    min_index = i
    for x in range(len(seq[i:])):
        current_index = x + i
        if seq[current_index] < seq[min_index]:
            min_index = current_index

    return min_index






