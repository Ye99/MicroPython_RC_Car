from setuptools import setup

setup(name='MicroPython_RC_Car',
      version='1.0',
      description='RC car remote control by ESP8266 and MicroPython.',
      url='https://github.com/Ye99/MicroPython_RC_Car',
      author='Ye Zhang',
      author_email='mr.yezhang@gmail.com',
      license='MIT',
      packages=['MicroPython_RC_Car'],
      install_requires=[
          'readchar',
      ],
      zip_safe=True)