

class TestStringUtils(unittest.TestCase):
    def test_capitilize(self):
        utils = StringUtils()
        self.assertEqual(utils.capitilize("skypro"), "Skypro")
        self.assertEqual(utils.capitilize("hello"), "Hello")
        self.assertEqual(utils.capitilize("python"), "Python")

if __name__ == '__main__':
    unittest.main()

    def test_trim(self):
        utils = StringUtils()
        self.assertEqual(utils.trim("   skypro"), "skypro")
        self.assertEqual(utils.trim("    hello    "), "hello")
        self.assertEqual(utils.trim("python   "), "python")

    def test_to_list(self):
        utils = StringUtils()
        self.assertEqual(utils.to_list("a,b,c,d"), ["a", "b", "c", "d"])
        self.assertEqual(utils.to_list("1:2:3", ":"), ["1", "2", "3"])
        self.assertEqual(utils.to_list("x;y;z", ";"), ["x", "y", "z"])

@pytest.mark.parametrize( 'string, containst, result', [(SkyPro, S, True), (SkyPro, J, False)] )
def test_contains(string, containst, result):
        string_utils = StringUtils()
        res = self.contains(string, containst)
        assert res == result
        