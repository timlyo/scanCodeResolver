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

"""
reads codes from /usr/include/linux/input.h for stuff and such
"""

import re
import sys

caching = False

def name_from_key(key):
    """ get the name(e.g. KEY_ESC) of the button from the key(number)
    :param code: int of key code
    :type code: int
    :return: button name
    :rtype: str
    """
    with open("/usr/include/linux/input.h") as file:
        #TODO handle multiple results
        line = re.findall("#define KEY_[a-zA-Z_0-9]+[\s]+" + str(key) + "[\n]", file.read())[0]
    name = line[8:line.find("\t")]
    return name

def key_from_name(name):
    """ get the key(number) of the button from the key name(e.g. KEY_ESC)
    :param name:
    :return:
    """
    with open("/usr/include/linux/input.h") as file:
        lines = re.findall("#define " + name + "[\s]+[0-9]*[\n]", file.read())

    if len(lines) == 0:
        raise ValueError("No key with name " + name + " was found")
    if len(lines) > 1:
        print("Got multiple results for " + name + ":" + repr(lines), file=sys.stderr)

    line = lines[0]
    key = line[line.rfind("\t") + 1:]
    return int(key)
