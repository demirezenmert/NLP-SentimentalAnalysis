from distutils.core import setup
import setuptools

setup(
  name = 'NLP-SentimentalAnalysis',
  packages = ['NLP-SentimentalAnalysis'], 
  version = '0.1',
  description = 'Detecting Sentimental Analysis',
  long_description=open('README.md', encoding="utf8").read(),
  long_description_content_type='text/markdown',
  author = 'Mert Demirezen',
  author_email = 'demirezenmert@gmail.com',
  url = 'https://github.com/demirezenmert/NLP-SentimentalAnalysis',
  keywords=['python', 'nlp', 'language processing'],
  install_requires = ["numpy"], 
  classifiers=[
        'Programming Language :: Python',
        'Environment :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)