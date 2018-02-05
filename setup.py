from setuptools import setup

setup(name='barbershop',
      version='0.1',
      description='A Python package that aids the user in making dynamic cuts to data in various parameter spaces, using a simple GUI.',
      url='https://github.com/ojhall94/barber',
      author='Oliver James Hall',
      author_email='ojh251@student.bham.ac.uk',
      license='MIT',
      packages=['barber'],
      install_requires=[
            'matplotlib',
            'pandas',
            'datetime',
            'numpy'
      ],
      zip_safe=False)
