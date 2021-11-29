#!/usr/bin/python
#
# Copyright 2021 Formal
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import unittest

# psycopg2 is only installed in its
# respective testing environments.

try:
    import psycopg2
except ImportError:
    psycopg2 = None


def run_unittests(module):
    testsuite = unittest.TestLoader().discover(module)
    result = unittest.TextTestRunner(verbosity=1).run(testsuite)
    sys.exit(any(result.failures or result.errors))


def main():
    if psycopg2:
        run_unittests('tests.psycopg2')
    else:
        run_unittests('tests.generic')


if __name__ == '__main__':
    main()
