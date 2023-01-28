from setuptools import setup, find_packages

setup(name='style_transfer',
      version='0.1',
      url='https://github.com/TimkaMLG/StyleTransfer',
      license='MIT',
      author='Timur Muradov',
      author_email='muradov.tr@phystech.edu',
      description='Style transfer python telegram bot',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['asyncio', 'telebot', 'numpy', 'torch', 'Pillow', 'setuptools'],
      install_requires=['asyncio', 'telebot', 'numpy', 'torch', 'Pillow', 'setuptools'])
