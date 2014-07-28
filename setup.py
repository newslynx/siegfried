from setuptools import setup, find_packages
from pip.req import parse_requirements
import os 

# hack for workings with pandocs
import codecs 
try: 
  codecs.lookup('mbcs') 
except LookupError: 
  ascii = codecs.lookup('ascii') 
  func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs') 
  codecs.register(func) 

# install readme
readme = os.path.join(os.path.dirname(__file__), 'readme.md')

try:
  import pypandoc
  description = pypandoc.convert(readme, 'rst', format='md')
except (IOError, ImportError):
  description = ""

# setup
setup(
  name='siegfried',
  version='0.2.0',
  description="Tools for taming lynx.",
  long_description = description,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='urls',
  author='Brian Abelson',
  author_email='brian@newslynx.org',
  url='http://github.com/newslynx/siegfried',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
    "beautifulsoup4>=4.3.2",
    "requests>=2.3.0",
    "tldextract>=1.4",
    "wsgiref>=0.1.2"
  ],
  tests_require=[]
)
