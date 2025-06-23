from setuptools import setup, find_packages

setup(
    name='youtube-downloader',
    version='0.1.0',
    author='GarosDev',
    description='Un descargador de videos de YouTube',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'yt-dlp>=2023.7.6',
        'pytube>=15.0.0',
        'requests>=2.31.0',
        'colorama>=0.4.6',
        'tqdm>=4.65.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
        ],
        'gui': [
            'tkinter',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'youtube-downloader=youtube_downloader.main:main',
        ],
    },
)