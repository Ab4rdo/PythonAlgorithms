
class BinarySearch:

    def search(self, seq, target):
        """
        Implementation of binary search algorithm
        seq - a int list
        target - a value to search
        return - index of target or raise ValueError if target not in the seq
        """

        if not seq:
            raise ValueError('List is empty')

        guess = int((len(seq)-1)/2)
        if target == seq[guess]:
            return guess
        if target > seq[guess]:
            return BinarySearch.search(seq[guess+1:], target)
        if target < seq[guess]:
            return BinarySearch.search(seq[seq[:guess-1]], target)
