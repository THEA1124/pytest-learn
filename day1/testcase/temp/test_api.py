import unittest


class TestApi(unittest.TestCase):

    def test_daa(self):
        print("立刻打印")

    def test_mashang(self):
        print("立刻打印")
        self.assertTrue(False)

    def test_dayin(self):
        print("life is tough")
        raise Exception("test111")

    @unittest.skip(reason="")
    def test_tough(self):
        print("难受")


if __name__=='__main__':
    print(ord('b'))
    print('___________')
    unittest.main()




