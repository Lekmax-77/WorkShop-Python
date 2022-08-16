# import pytest
import Exercice_1
import Exercice_2
import Exercice_8

# import sys
# from io import StringIO
# from unittest import TestCase
# from unittest.mock import patch
import pytest

class TestErrors(TestCase):
    def test_first_exercise(capsys):
        test_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"
        exercise_one()
        captured = capsys.readouterr()
        assert captured.out == test_output

    def test_second_exercise(capsys):
        exercise_two(263)
        captured = capsys.readouterr()
        assert captured.out == "263 --> true\n"
        exercise_two(236)
        captured = capsys.readouterr()
        assert captured.out == "236 --> false\n"
        exercise_two(2532)
        captured = capsys.readouterr()
        assert captured

    def test_to_str():
        assert add(5, 30) == '35'
        assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'

    def test_nine_exericise():
        # TODO : Tester la fonction de malek
        pass

# if __name__ == '__main__':
#     unittest.main()
