from setuptools import setup, find_packages

setup(
    name='unreal_engine_development_python_utilities',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python_logging @ git+https://github.com/Mythical-Github/general_python_utilities.git',
    ],
    include_package_data=True,
    package_data={},
    description='A Python module containing unreal engine development related functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/unreal_engine_development_python_utilities',
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL3',
)
