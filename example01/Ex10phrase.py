phrase = input("Set a phrase: ")

class TestPhrase:
    def test_check_math(self):
        test_len = 15
        assert len(phrase) == test_len, f"Your phrase is {len(phrase)} symbols"