# setup.py

from setuptools import setup, find_packages
setup(
    name='graphics_planes',
    version='1.0.1',
    description='Esta es una libreria para generar graficos en 2D, añadiendo herramientas y utilidades extras para mejorar la generacion de graficos.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CCFTS/graphics-plane',
    author='Damian Zsiros, Alejandro Beltran, Alejandro de La Esprella, Cristian Cuadrado',
    
    
    author_email='damjeronzalez23@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    
    python_requires='>=3.6',
    packages=find_packages(),

)
