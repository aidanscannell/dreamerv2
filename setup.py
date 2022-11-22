import setuptools
import pathlib

# python_requires = "~=3.7"

install_requires=[
    'gym[atari]',
    'atari_py',
    'crafter',
    'dm_control',
    'ruamel.yaml',
    # 'tensorflow==2.6.4',
    # 'tensorflow',
    "tensorflow==2.4.2; platform_system!='Darwin' or platform_machine!='arm64'",
    "tensorflow-macos==2.4.2; platform_system=='Darwin' and platform_machine=='arm64'",
    'tensorflow_probability==0.12.2',
    'learn2learn',
],
extras_require = {
    "experiments": ["hydra-core", "palettable", "tikzplotlib"],
    "examples": ["jupyter", "hydra-core"],
    "dev": ["black[jupyter]", "pre-commit", "pyright", "isort", "pyflakes", "pytest"],
}

setuptools.setup(
    name='dreamerv2',
    version='2.2.0',
    description='Mastering Atari with Discrete World Models',
    url='http://github.com/danijar/dreamerv2',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['dreamerv2', 'dreamerv2.common'],
    package_data={'dreamerv2': ['configs.yaml']},
    entry_points={'console_scripts': ['dreamerv2=dreamerv2.train:main']},
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    # python_requires=python_requires,
    install_requires=install_requires,
    extras_require=extras_require,
)
