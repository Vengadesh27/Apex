from setuptools import setup, find_packages

setup(
    name='apex',  # Replace with your package name
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click', 
    ],
    entry_points={
        'console_scripts': [
            'apex=apex.cli:create',  
        ],
    },
    include_package_data=True,
    description='A web frame work for creating faster web applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Vengadesh27/Apex.git', 
    author='Vengadesh',
    author_email='m.vengadesh2019@gmail.com',
    license='MIT',  
)
