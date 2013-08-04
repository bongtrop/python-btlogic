from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-btlogic",
      version="0.2.0",
      py_modules=["btlogic"],
      description="Libraries for management logic term",
      author="Pongsakorn Sommalai",
      author_email = "bongtrop@gmail.com",
      license="BSD",
      url="https://github.com/bongtrop/python-btlogic",
      long_description=long_description,
      platforms=["any"]
      )

