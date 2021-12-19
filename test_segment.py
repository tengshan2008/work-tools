import unittest
from segment import Segment


class SegmentTest(unittest.TestCase):
    user_dict = ['我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '物', '园', '玩']
    sentence = '我们在野生动物园玩'

    def setUp(self) -> None:
        self.segment = Segment(self.user_dict)
        return super().setUp()

    def test_fmm(self):
        result = self.segment.FMM(self.sentence)
        print(result)

    def test_bmm(self):
        result = self.segment.BMM(self.sentence)
        print(result)

    def test_two_match(self):
        result = self.segment.merge_match(self.sentence)
        print(result)
