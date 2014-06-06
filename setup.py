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
  description = pypandoc.convert(readme, 'rst')
except (IOError, ImportError):
  description = ""


# setup
setup(
  name='newslynx-url',
  version='0.0.8',
  description="tools for parsing, extracting, reconciling, and unshortening urls",
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
  url='http://github.com/newslynx/newslynx-urls',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
    "lxml==3.3.5",
    "tldextract==1.4"
  ],
  tests_require=[]
)
