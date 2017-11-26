

def sort(seq):
    """
    Implementation of insertion sort algorithm
    :param seq: a integer list
    :return: new ascending sorted list
    """

    if not seq:
        raise ValueError('The list is empty')

    for next in enumerate(seq[1:]):
        curr = next[0] + 1
        temp = next[1]

        while curr > 0 and temp < seq[curr-1]:
            seq[curr] = seq[curr-1]
            curr -= 1

        seq[curr] = temp

    return seq