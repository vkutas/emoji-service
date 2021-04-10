from setuptools import find_packages
from setuptools import setup

setup(
    name='Emoji Service',
    description="Enterprise Grade Emoji Provider!",
    author='vkutas',
    url='',
    packages=find_packages('src'),
    package_dir={
        '': 'src'},
    include_package_data=True,
    keywords=[
        'web_app', 'emoji', 'flask'
    ],
    entry_points={
        'console_scripts': [
            'web_server = app:main']},
)