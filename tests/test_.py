import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pass_gen


special_chars = ['*','$','#','@','&','~','%']
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def test_generation():
    test_1 = pass_gen.generate_pass(special_chars =special_chars, numbers=numbers, letters=letters)
    test_2 = pass_gen.generate_pass(special_chars =special_chars, numbers=numbers, letters=letters)
    test_3 = pass_gen.generate_pass(special_chars =special_chars, numbers=numbers, letters=letters)
    test_4 = pass_gen.generate_pass(special_chars =special_chars, numbers=numbers, letters=letters)
    assert len(test_1) == 16
    print("test 1 (" + test_1 + " ) length is 16 ")
    assert len(test_2) == 16
    print("test 1 (" + test_2 + " ) length is 16 ")
    assert len(test_3) == 16
    print("test 1 (" + test_3 + " ) length is 16 ")
    assert len(test_4) == 16
    print("test 1 (" + test_4 + " ) length is 16 ")
