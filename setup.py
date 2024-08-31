# setup.py

from setuptools import setup, find_packages

def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()
setup(
    name='graphics_planes',
    version='1.0.2',
    description='Esta es una libreria para generar graficos en 2D, añadiendo herramientas y utilidades extras para mejorar la generacion de graficos.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/CCFTS/graphics-plane',
    author='Damian Zsiros',
    author_email='damjeronzalez23@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    
    python_requires='>=3.6',
    packages=find_packages(),
    maintainer="Alejandro Beltran, Cristian Cuadrado",
    install_requires=[
        'setuptools==74.0.0',
        'twine==5.1.1',
        'svg_turtle==0.4.2',
        'svgwrite==1.4.3',
        'PythonTurtle==0.3.2',
    ],

)
