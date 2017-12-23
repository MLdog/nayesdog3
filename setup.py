from setuptools import setup
version = '0.1.5.1'
setup(
    name = 'nayesdog',
    packages = ['nayesdog'],
    version = version,
    description = 'RSS reader with Naive Bayes powered recommendations',
    author = 'Ilya Prokin, Sergio Peignier',
    author_email = 'isprokin@gmail.com, sergio.peignier.zapata@gmail.com',
    url = 'http://github.com/MLdog/nayesdog3',
    download_url = 'https://github.com/MLdog/nayesdog3/archive/v{}.tar.gz'.format(version),
    keywords = ['RSS reader', 'Naive Bayes', 'recommendations'],
    classifiers = [],
    #package_data = {'nayesdog':['icons/*','css.css','stopwords.txt']},
    include_package_data=True,
    entry_points = """
      [console_scripts]
      nayesdog = nayesdog.command_line:main
    """,
    install_requires=['feedparser', 'beautifulsoup4'],
    #scripts=['bin/nayesdog'],
)
