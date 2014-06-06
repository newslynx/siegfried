![travis-img](https://travis-ci.org/newslynx/siegfried.svg)

# siegfried

_Tools for taming lynx._

## Install
```
pip install siegfried
```

## Test
requires `nose`
```
nosetests
```

## Usage

This module contains various methods that are used throughout `newslnyx`.
but the main functions are `unshorten_url`, `is_article_url`, and `prepare_url`:

```python
from siegfried import (
  unshorten_url, is_article_url, prepare_url
)

print unshorten_url('bit.ly/1j3SrUC')
# http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism/

print is_article_url(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism'
  )
# True

print is_article_url(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism',
  pattern = r'.*towcenter\.org/blog/.*'
)
# True

import re
pattern = re.compile(r'.*towcenter\.org/blog/.*')
print is_article_url(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism',
  pattern = pattern
)
# True

print prepare_url(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism/?q=lfjad&f=lkfdjsal'
  )
# http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism
```