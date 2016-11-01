from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='assess_composition',
      version='0.1',
      description='Tools to assess the composition quality of video shots',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='video quality composition aesthetics',
      url='',
      author='Rosie Campbell',
      author_email='rosie.campbell@bbc.co.uk',
      license='',
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=[
          'numpy',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['assess_composition = assess_composition.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
