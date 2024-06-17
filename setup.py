#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

from sentry_telegram import __version__


setup(
    name='sentry_telegram',
    version=__version__,
    packages=['sentry_telegram'],
    url='https://github.com/EugineKh/sentry-telegram',
    author='EugineKh',
    description='Plugin for Sentry which allows sending notification via Telegram messenger.',
    license='MIT',
    entry_points={
        'sentry.plugins': [
            'sentry_telegram = sentry_telegram.plugin:TelegramNotificationsPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: System :: Monitoring',
    ],
    include_package_data=True,
)
