from setuptools import setup

setup(name='joypy',
      version='0.1.3',
      description='Joyplots in python',
      long_description='Joyploy in python.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      url='http://github.com/sbebo/joypy',
      author='Leonardo Taccari',
      author_email='leonardo.taccari@gmail.com',
      license='MIT',
      packages=['joypy'],
      install_requires=[
          'matplotlib',
          'numpy',
          'scipy>=0.11.0',
          'pandas>=0.20.0'
      ],
      zip_safe=False)
