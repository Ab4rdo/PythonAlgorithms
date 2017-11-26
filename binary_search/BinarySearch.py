

def search(seq, target):
        """
        Implementation of binary_search search algorithm
        seq - a int list
        target - a value to search
        return - index of target or raise ValueError if target not in the seq or if seq is empty
        """

        if not seq:
            raise ValueError('List is empty or the target is not in the list')

        guess = int((len(seq))/2)
        if target == seq[guess]:
            return guess
        if target > seq[guess]:
            return guess + 1 + search(seq[guess+1:], target)
        if target < seq[guess]:
            return search(seq[:guess], target)
