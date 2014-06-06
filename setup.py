from setuptools import setup, find_packages
from pip.req import parse_requirements
import os 


readme = os.path.join(os.path.dirname(__file__), 'readme.md')
try:
  import pypandoc
  description = pypandoc.convert(readme, 'rst')
except IOError, ImportError:
  description = open(readme, 'rb').read()

install_reqs = [
  str(ir.req) for ir in parse_requirements('requirements.txt')
  ] 

setup(
  name='newslynx-url',
  version='0.0.4',
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
  install_requires=install_reqs,
  tests_require=[]
)
