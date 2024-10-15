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

if sys.version_info.major <= 2:
    import urllib
    url_quote_fn = urllib.quote
else:
    import urllib.parse
    url_quote_fn = urllib.parse.quote


def generate_sql_comment(endUserID):
    """
    Return a SQL comment with endUserID
    """
    if endUserID == '' or endUserID == None:  # No entries added.
        return ''

    return '/*formal_role_id:{0}*/ '.format(url_quote(endUserID))


def url_quote(s):
    if not isinstance(s, (str, bytes)):
        return s
    quoted = url_quote_fn(s)
    # Since SQL uses '%' as a keyword, '%' is a by-product of url quoting
    # e.g. foo,bar --> foo%2Cbar
    # thus in our quoting, we need to escape it too to finally give
    #      foo,bar --> foo%%2Cbar
    return quoted.replace('%', '%%')
