import random

"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one
 number ‘x’. You have to find ‘x’. The input array is not sorted.
"""


class MissingNumbers:

    @staticmethod
    def sum_1_n(n: int) -> int:
        assert n >= 1
        return n * (n + 1) // 2

    @staticmethod
    def find_missing(search: list, n: int) -> int:
        assert len(search) >= 2
        assert n > 1
        total = sum(search)
        return MissingNumbers.sum_1_n(n) - total

    @staticmethod
    def find_missing_set(search: list, n: int) -> int:
        diff = set(range(1, n+1, 1)) - set(search)
        assert len(diff) == 1
        return diff.pop()


if __name__ == "__main__":
    length = random.randint(2, 20)
    my_list = list(range(1, length))
    my_n = length - 1

    random.shuffle(my_list)
    my_list.pop()  # pop the last

    print("List is {length} long and is from 1 to {n}".format(length=len(my_list), n=my_n))
    print(my_list)
    print("Missing number is {}".format(MissingNumbers.find_missing(my_list, my_n)))
    # python solution
    print("Set diff is {}".format(MissingNumbers.find_missing_set(my_list, my_n)))
