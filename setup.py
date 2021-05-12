from setuptools import setup, find_packages

setup(
    name='jetracer',
    version='0.0.0',
    description='AI racecar based on NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'adafruit-circuitpython-servokit'
    ],
)
