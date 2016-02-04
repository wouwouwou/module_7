class Sorter(object):
    """
    Base class for sorters. Defines the `sort` method.
    """
    def sort(self, elements):
        """
        Sorts the elements in the list.

        :param elements: The list of elements which has to be sorted
        :type elements: list
        :return: The sorted list of elements
        :rtype: list
        """
        raise NotImplementedError()


class InsertionSorter(Sorter):
    """
    Sorter implementation using the insertion sort strategy.
    """
    def sort(self, elements):
        # Replace this with a useful piece of code that actually sorts elements
        # the test assumes that you return something
        return elements


class QuickSorter(Sorter):
    """
    Sorter implementation using the quick sort strategy.
    """
    def sort(self, elements):
        # Replace this with a useful piece of code that actually sorts elements
        # the test assumes that you return something
        return elements
