import unittest
import os

from newslynx_urls import *

TEST_DIR = os.path.abspath(os.path.dirname(__file__))

class Tests(unittest.TestCase):
  
  def test_get_domain(self):
    case = 'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html?hp&_r=0'
    assert(get_domain(case) == 'www.nytimes.com')

  def test_get_simple_domain(self):
    case = 'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html?hp&_r=0'
    assert(get_simple_domain(case) == 'nytimes')

  def test_remove_args(self):
    case = 'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html?hp&_r=0'
    assert(remove_args(case) == 'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html')

  def test_is_article_url(self):
    test_fp = os.path.join(TEST_DIR, 'fixtures/article_urls.txt')
    with open(test_fp, 'rb') as f:
      for case in f.read().split('\n'):
        print case
        items = case.split(',')
        tf = items[0]
        url = items[1]
        truth_val = True if tf == '1' else False
        assert(is_article_url(url) == truth_val)

  def test_url_to_slug(self):
    case = 'http://www.nytimes.com/video/movies/100000002920951/anatomy-8216the-fault-in-our-stars8217.html?smid=tw-nytimes'
    assert(url_to_slug(case) == '100000002920951-anatomy-8216the-fault-in-our-stars8217')

  def test_prepare_url(self):
    cases = [
      ('http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html?hp&_r=0',
       'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report.html'),
      ('http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report/index.html',
        'http://www.nytimes.com/2014/06/06/business/gm-ignition-switch-internal-recall-investigation-report')
    ]
    for c in cases:
      test, truth = c 
      assert(prepare_url(test) == truth)
  
  def test_is_short_url(self):
    cases = [
      '1.usa.gov/1kEeAcb',
      'bit.ly/1kzIQWw',
      'http://1.usa.gov/1kEeAcb'
    ]
    for c in cases:
      assert(is_short_url(c))

  def test_unshorten(self):
    cases = [
      ('http://nyti.ms/1oxYm3e',
      'http://www.nytimes.com/video/movies/100000002920951/anatomy-8216the-fault-in-our-stars8217.html'),
      ('nyti.ms/1oxYm3e',
      'http://www.nytimes.com/video/movies/100000002920951/anatomy-8216the-fault-in-our-stars8217.html'),   
      ('http://bit.ly/1kzIQWw',
       'http://www.fromscratchradio.com/show/marc-dacosta'),
      ('bit.ly/aaaaaa', 'http://bit.ly/aaaaaa')
      ]
    for c in cases:
      test, truth = c 
      try:
        test = prepare_url(unshorten(test))
        assert(test == truth)
      except AssertionError:
        print "failed on %s" % test 
        raise
