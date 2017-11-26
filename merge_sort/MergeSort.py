
def sort(seq):
    """
    Implementation of simplest merge sort function
    :param seq: a integer list
    :return: new ascending sorted list or raise ValueError is seq is empty
    """

    if not seq:
        raise ValueError('Empty list')

    if len(seq) <= 1:
        return seq[:len(seq)]

    m = int(len(seq)/2)
    return merge(sort(seq[:m]), sort(seq[m:]))


# Helping functions


def merge(seq1, seq2):
    """
    Implementation of merging function for merge sort
    :param seq1: a first integer list
    :param seq2: a second integer list
    :return: merged and sorted list made of seq1 and seq2
    """

    len1 = len(seq1)
    len2 = len(seq2)
    result = seq1 + seq2

    i = j = k = 0

    while i < len1 and j < len2:
        if seq1[i] < seq2[j]:
            result[k] = seq1[i]
            k += 1
            i += 1
        else:
            result[k] = seq2[j]
            k += 1
            j += 1

    while i < len1:
        result[k] = seq1[i]
        k += 1
        i += 1

    while j < len2:
        result[k] = seq2[j]
        k += 1
        j += 1

    return result
