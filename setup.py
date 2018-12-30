from distutils.core import setup
setup(
  name = 'pydemoji',
  packages = ['pydemoji'],
  version = '0.0.1',
  license= 'MIT',
  description = 'API Wrapper for DiscordEmoji',
  author = 'Luke J',
  author_email = 'itsnotluke@outlook.com',
  url = 'https://github.com/paixlukee/DiscordEmoji-Wrapper',
  download_url = 'https://github.com/paixlukee/DiscordEmoji-Wrapper/archive/0.0.1.tar.gz',
  keywords = ['apiwrapper', 'discordemoji'],
  install_requires=[
          'aiohttp',
          'json'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
