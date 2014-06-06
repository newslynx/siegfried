newslynx-urls
========
A newslynx-opinionated collection of utilities for dealing with urls.


## Install
```
git clone http://github.com/newslynx/newslynx-urls.git
pip install -e newslynx-urls
```

## Test
requires `nose`
```
nosetests
```

## Usage

This module contains various methods that are used throughout `newslnyx-core`.
but the main functions are `unshorten_url`, `is_article`, and `prepare_url`:

```python
from newslynx_urls import (
  unshorten_url, is_article, prepare_url
)

print unshorten_url('bit.ly/1j3SrUC')
# http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism

print is_article(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism'
  )
# True

print is_article(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism',
  pattern = r'.*towcenter\.org/blog/.*'
)
# http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism

print prepare_url(
  'http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism/?q=lfjad&f=lkfdjsal'
  )
# http://towcenter.org/blog/tow-fellows-brian-abelson-and-michael-keller-to-study-the-impact-of-journalism
```