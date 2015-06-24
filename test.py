"""
Copyright 2015 Tim Maddison

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import unittest
import scanCode

class Tests(unittest.TestCase):
    def test_key_G(self):
        self.assertEqual(34, scanCode.key_from_name("KEY_G"))

    def test_key_Z(self):
        self.assertEqual(44, scanCode.key_from_name("KEY_Z"))

    def test_key_comma(self):
        self.assertEqual(51, scanCode.key_from_name("KEY_COMMA"))

    def test_code_comma(self):
        self.assertEqual("KEY_COMMA", scanCode.name_from_key(51))

if __name__ == '__main__':
    unittest.main()
