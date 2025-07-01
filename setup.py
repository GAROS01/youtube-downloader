from setuptools import setup, find_packages

setup(
    name='youtube-downloader',
    version='0.1.0',
    author='GarosDev',
    description='Un descargador de videos de YouTube',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'yt-dlp>=2025.6.9',
        'pytubefix>=8.8.4',
        'requests>=2.31.0',
        'colorama>=0.4.6',
        'tqdm>=4.65.0',
    ],
    extras_require={
        'dev': [
            'pytest>=8.4.1',
            'pytest-cov>=6.2.1',
            'black>=25.1.0',
            'flake8>=7.3.0',
            'setuptools>=80.9.0',
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
    license='MIT',
    entry_points={
        'console_scripts': [
            'youtube-downloader=youtube_downloader.main:main',
        ],
    },
)