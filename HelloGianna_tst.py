import unittest
from HelloGianna import HelloGianna

class MyTestCase(unittest.TestCase):
  def test_default_greeting_set(self):
    hw = HelloGianna()
    self.assertEqual(hw.message, 'Hello world!')

if __name__ == '__main__':
  unittest.main()
