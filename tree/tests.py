import base
import unittest


class MorseCodeTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        tree = base.MorseCodeTree()
        self.tree = tree
        node = base.Node
        tree.root.l = node('e')
        tree.root.r = node('t')
        tree.root.l.l = node('i')
        tree.root.l.r = node('a')
        tree.root.l.l.l = node('s')
        tree.root.l.l.r = node('u')
        tree.root.l.l.l.l = node('h')
        tree.root.l.l.l.r = node('v')
        tree.root.l.l.l.l.l = node('5')
        tree.root.l.l.l.l.r = node('4')
        tree.root.l.l.l.r.r = node('3')
        tree.root.l.l.l.r.r = node('3')
        tree.root.l.l.r.l = node('f')
        tree.root.l.l.r.r = node('')
        tree.root.l.l.r.r.r = node('2')
        tree.root.l.r.l = node('r')
        tree.root.l.r.r = node('w')
        tree.root.l.r.l.l = node('l')
        tree.root.l.r.l.r = node('')
        tree.root.l.r.l.r.l = node('+')
        tree.root.l.r.r.l = node('p')
        tree.root.l.r.r.r = node('j')
        tree.root.l.r.r.r.r = node('1')
        tree.root.r.l = node('n')
        tree.root.r.r = node('m')
        tree.root.r.l.l = node('d')
        tree.root.r.l.r = node('k')
        tree.root.r.l.l.l = node('b')
        tree.root.r.l.l.r = node('x')
        tree.root.r.l.l.l.l = node('6')
        tree.root.r.l.l.l.r = node('=')
        tree.root.r.l.l.r.l = node('/')
        tree.root.r.l.r.l = node('c')
        tree.root.r.l.r.r = node('y')
        tree.root.r.r.l = node('g')
        tree.root.r.r.r = node('o')
        tree.root.r.r.l.l = node('z')
        tree.root.r.r.l.r = node('q')
        tree.root.r.r.l.l.l = node('7')
        tree.root.r.r.r.l = node('')
        tree.root.r.r.r.r = node('')
        tree.root.r.r.r.l.l = node('8')
        tree.root.r.r.r.r.l = node('9')
        tree.root.r.r.r.r.r = node('0')

    def test_decode_letter(self):
        self.assertEqual(self.tree.DecodeLetter('.-'), 'a')

    def test_decode_word(self):
        self.assertEqual(self.tree.DecodeWord('.- .- .-'), 'aaa')

    def test_decode(self):
        self.assertEqual(self.tree.Decode('.- .- .-   .- .- .-'), 'aaa aaa')

    def test_big_decode(self):
        self.assertEqual(self.tree.Decode(
            '- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. . -.. / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.'), 'the quick brown fox jumped over the lazy dog')

    def test_not_in_tree_decode_letter(self):
        self.assertIsNone(self.tree.DecodeLetter('.......'))


if __name__ == "__main__":
    unittest.main()
