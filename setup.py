from setuptools import setup

# python setup.py sdist
setup(
    name='Password_validators',
    author='Mateusz Mogielski',
    author_email='mogielski@protonmail.com',
    version='0.1.0',
    description='Collection of password validators',
    license='MIT',
    packages=['password_validators'],
    install_requires=['requests'],
)
