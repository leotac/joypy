from setuptools import setup

setup(name='joypy',
      version='0.2.5',
      description='Joyplots in python',
      long_description='Joyplots in python.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      url='http://github.com/sbebo/joypy',
      author='Leonardo Taccari',
      author_email='leonardo.taccari@gmail.com',
      license='MIT',
      packages=['joypy'],
      python_requires='>=3.5',
      install_requires=[
          'numpy>=1.16.5',
          'scipy>=0.11.0',
          'pandas>=0.20.0',
          'matplotlib',
      ],
      zip_safe=False)
