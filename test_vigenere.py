import unittest
from vigenere import vigenere_cipher

class TestVigenereCipher(unittest.TestCase):

    def test_basic_encrypt(self):
        self.assertEqual(vigenere_cipher("HELLO", "KEY"), "RIJVS")

    def test_basic_decrypt(self):
        self.assertEqual(vigenere_cipher("RIJVS", "KEY", mode='decrypt'), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(vigenere_cipher("HelloWorld", "Key"), "RijvsUyvjn")
        self.assertEqual(vigenere_cipher("RijvsUyvjn", "Key", mode='decrypt'), "HelloWorld")

    def test_non_alpha_characters(self):
        text = "Hello, World!"
        encrypted = vigenere_cipher(text, "KEY")
        decrypted = vigenere_cipher(encrypted, "KEY", mode='decrypt')
        self.assertEqual(decrypted, text)

    def test_empty_string(self):
        self.assertEqual(vigenere_cipher("", "KEY"), "")

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            vigenere_cipher("HELLO", "K3Y")

if __name__ == '__main__':
    unittest.main()
