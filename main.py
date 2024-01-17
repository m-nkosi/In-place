import unittest


def bubble_to_the_back(index: int, length: int, array: list[int]) -> None:
    """Bubble the element in the array: Helper function to RemoveDuplicates method"""
    if index != (length - 1):
        array[index], array[index+1] = array[index+1], array[index]
        index += 1
        bubble_to_the_back(index, length, array)


def remove_duplicates(nums: list[int]) -> int:
    k = 0
    i = 0
    length = len(nums)
    while i < (length-1-k):
        if nums[i] == nums[i+1]:
            bubble_to_the_back(i+1, length, nums)
            k += 1
        else:
            i += 1
    return k


class TestBubble(unittest.TestCase):

    def test_bubble_case_one(self):
        array = [1, 2, 3, 4, 5]
        bubble_to_the_back(0, len(array), array)
        self.assertEqual(array, [2, 3, 4, 5, 1])

    def test_bubble_case_two(self):
        array = [2, 5, 10, 5, 10]
        bubble_to_the_back(1, len(array), array)
        self.assertEqual(array, [2, 10, 5, 10, 5])

    def test_bubble_case_moving_last(self):
        array = [1, 2]
        bubble_to_the_back(1, len(array), array)
        self.assertEqual(array, [1, 2])


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_case_one(self):
        array = [1, 1, 2]
        array_copy = array.copy()
        k = remove_duplicates(array)
        with self.subTest(f"Testing if the array {array_copy} duplicates were removed"):
            self.assertEqual(array[:2], [1, 2])
        with self.subTest(f" Testing if the array {array_copy} number of duplicates is correct"):
            self.assertEqual(k, 1)

    def test_remove_duplicates_case_two(self):
        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        array_copy = array.copy()
        k = remove_duplicates(array)
        with self.subTest(f"Testing if the array {array_copy} duplicates were removed"):
            self.assertEqual(array[:5], [0, 1, 2, 3, 4])
        with self.subTest(f"Testing if the array's {array_copy} number of duplicates is correct"):
            self.assertEqual(k, 5)


if __name__ == '__main__':
    unittest.main()
