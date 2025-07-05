.. image:: https://github.com/davewalker5/NetworkCalculator/workflows/Python%20CI%20Build/badge.svg
    :target: https://github.com/davewalker5/NetworkCalculator/actions
    :alt: Build Status

.. image:: https://codecov.io/gh/davewalker5/NetworkCalculator/branch/main/graph/badge.svg?token=1E72RZU3CQ
    :target: https://codecov.io/gh/davewalker5/NetworkCalculator
    :alt: Coverage

.. image:: https://sonarcloud.io/api/project_badges/measure?project=davewalker5_NetworkCalculator&metric=alert_status
    :target: https://sonarcloud.io/summary/new_code?id=davewalker5_NetworkCalculator
    :alt: Quality Gate

.. image:: https://img.shields.io/github/issues/davewalker5/NetworkCalculator
    :target: https://github.com/davewalker5/NetworkCalculator/issues
    :alt: GitHub issues

.. image:: https://img.shields.io/github/v/release/davewalker5/NetworkCalculator.svg?include_prereleases
    :target: https://github.com/davewalker5/NetworkCalculator/releases
    :alt: Releases

.. image:: https://img.shields.io/badge/License-mit-blue.svg
    :target: https://github.com/davewalker5/NetworkCalculator/blob/main/LICENSE
    :alt: License

.. image:: https://img.shields.io/badge/language-python-blue.svg
    :target: https://www.python.org
    :alt: Language

.. image:: https://img.shields.io/github/languages/code-size/davewalker5/NetworkCalculator
    :target: https://github.com/davewalker5/NetworkCalculator/
    :alt: GitHub code size in bytes


Network Calculator
==================

The Network Calculator is an application written in Python for calculating network properties and calculating subnets. It has
the following components:

- A Flask-based REST API for performing the calculations
- A simple client for applications calling the REST API
- A simple command-line application that uses the API to perofm


Structure
=========

+-------------------------------+----------------------------------------------------------------------+
| **Package**                   | **Contents**                                                         |
+-------------------------------+----------------------------------------------------------------------+
| api                           | Flask-based REST API                                                 |
+-------------------------------+----------------------------------------------------------------------+
| cli                           | Command-line client (requires a running API)                         |
+-------------------------------+----------------------------------------------------------------------+
| client                        | Simple client wrapper to allow applications to call the API          |
+-------------------------------+----------------------------------------------------------------------+
| common                        | Common code used by the network calculation functions                |
+-------------------------------+----------------------------------------------------------------------+
| ipv4                          | IPv4 network details and subnetting implementation                   |
+-------------------------------+----------------------------------------------------------------------+
| logging_wrapper               | Logging wrapper used by the API to write application logs            |
+-------------------------------+----------------------------------------------------------------------+


REST API Endpoints
==================

/ipv4/network
-------------

Returns the following details for the network specified in the request body:

- Network address
- Subnet mask
- Broadcast address
- First host IP address
- Last host IP address

The request body is in text/json format can be supplied in one of two forms, depending on the format in which the IP address is specified:

::

    {
        "ip_address": "172.16.35.123",
        "subnet_mask": "255.255.240.0"
    }

or:

::

    {
        "ip_address": "172.16.35.123/20"
    }

Requests are sent using the POST verb.

A typical response is:

::

    [
        {
            "broadcast": [172, 16, 47, 255],
            "broadcast_binary": ["10101100", "00010000", "00101111", "11111111"],
            "first": [172, 16, 32, 1],
            "first_binary": ["10101100", "00010000", "00100000", "00000001"],
            "last": [172, 16, 47, 254],
            "last_binary": ["10101100", "00010000", "00101111", "11111110"],
            "network": [172, 16, 32, 0],
            "network_binary": ["10101100", "00010000", "00100000", "00000000"],
            "network_bits": 20,
            "subnet": [255, 255, 240, 0],
            "subnet_binary": ["11111111", "11111111", "11110000", "00000000"]
        }
    ]


/ipv4/subnet
------------

Given an IP address and a subnet mask (or number of network bits) and a number of hosts or networks, calculate the subnet details for subnetting the supplied IP into one of:

- A set of subnets each of which can support a specified number of hosts
- A specified number of subnets, each supporting as many hosts as possible
- A set of subnets with a specified number of network bits, each supporting as many hosts as possible

Subnets Supporting a Specified Number of Hosts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request body is in text/json format and can be supplied in several forms, depending on the format in which the IP address is specified:

::

    {
        "ip_address": "10.1.1.0",
        "subnet_mask": "255.255.255.0",
        "hosts": 14
    }

or:

::

    {
        "ip_address": "10.1.1.0/24",
        "hosts": 14
    }

Requests are sent using the POST verb.

Subnet Into a Specified Number of Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request body is in text/json format and can be supplied in several forms, depending on the format in which the IP address is specified:

::

    {
        "ip_address": "10.128.192.0",
        "subnet_mask": "255.255.192.0",
        "networks": 30
    }

or:

::

    {
        "ip_address": "10.128.192.0/18",
        "networks": 30
    }

Requests are sent using the POST verb.

Subnet Based on a Number of Network Bits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request body is in text/json format and can be supplied in several forms, depending on the format in which the IP address is specified:

::

    {
        "ip_address": "192.168.1.96",
        "subnet_mask": "255.255.255.240",
        "network_bits": 30
    }

or:

::

    {
        "ip_address": "192.168.1.96/28",
        "network_bits": 30
    }

Requests are sent using the POST verb.

Response
--------

A typical response is as follows:

::

    [
        {
            "network_bits": 23,
            "networks": [
                {
                    "broadcast": [10, 128, 193, 255],
                    "broadcast_binary": ["00001010", "10000000", "11000001", "11111111"],
                    "first": [10, 128, 192, 1],
                    "first_binary": ["00001010", "10000000", "11000000", "00000001"],
                    "last": [10, 128, 193, 254],
                    "last_binary": ["00001010", "10000000", "11000001", "11111110"],
                    "network": [10, 128, 192, 0],
                    "network_binary": ["00001010", "10000000", "11000000", "00000000"]
                },
                :
                :
            ]
        }
    ]

The "networks" element of the response is a list of network details for each of the calculated subnets.


/ipv4/samesubnet
----------------

Determines whether or not two IP addresses are on the same subnet. The request body is in text/json format and can be supplied in several forms, depending on the format in which the IP address is specified:

::

    {
        "ip_address_1": "10.1.255.1",
        "ip_address_2": "10.1.128.2",
        "subnet_mask": "255.255.128.0"
    }

or:

::

    {
        "ip_address_1": "10.1.255.1/17",
        "ip_address_2": "10.1.128.2/17"
    }

Requests are sent using the POST verb.

A typical response is as follows:

::

    {
        "same_subnet": true
    }


Running the Application
=======================

Pre-requisites
--------------

To run the application, a virtual environment should be created, the requirements should be installed using pip and the
environment should be activated.


Running the REST API and CLI
----------------------------

To run the REST API in the Flask development web server, enter the following from the root of the project:

::

    export PYTHONPATH=`pwd`/src
    export FLASK_DEBUG=1
    python -m api

The first two commands will need to be modified based on the current operating system. Once the development server
is running, use the following commands in another terminal window to run the CLI:

::

    export PYTHONPATH=`pwd`/src
    python -m cli http://127.0.0.1 5000

The arguments are the host name and protocol for the API and the port number it's listening on, which default to the values shown.

Once the CLI is running, the following should be displayed:

::

    API Host: http://127.0.0.1
    API Port: 5000

    1: Calculate Network Details
    2: Subnetting
    3: Same Subnet

    Which calculation do you want to do?

As an example, enter 2 and, when prompted, enter the following values:

+--------------------+-------------+
| Property           | Value       |
+--------------------+-------------+
| IP Address         | 10.1.1.0/24 |
+--------------------+-------------+
| Subnet Mask        | Blank       |
+--------------------+-------------+
| Number of Hosts    | 14          |
+--------------------+-------------+
| Number of Networks | 0           |
+--------------------+-------------+

In this example:

- The subnet mask isn't needed because the IP address has the /24 suffix, that specifies the length of the network prefix
- The number of networks is entered as 0 because we're subnetting for a number of hosts per network, not a number of networks

The following should be the output:

::

    Subnet Mask       : 255.255.255.240
    Network Bits      : 28

    #  Network            First Host         Last Host          Broadcast
    -  -------            ----------         ---------          ---------
    1  10.1.1.0           10.1.1.1           10.1.1.14          10.1.1.15
    2  10.1.1.16          10.1.1.17          10.1.1.30          10.1.1.31
    3  10.1.1.32          10.1.1.33          10.1.1.46          10.1.1.47
    4  10.1.1.48          10.1.1.49          10.1.1.62          10.1.1.63
    5  10.1.1.64          10.1.1.65          10.1.1.78          10.1.1.79
    6  10.1.1.80          10.1.1.81          10.1.1.94          10.1.1.95
    7  10.1.1.96          10.1.1.97          10.1.1.110         10.1.1.111
    8  10.1.1.112         10.1.1.113         10.1.1.126         10.1.1.127
    9  10.1.1.128         10.1.1.129         10.1.1.142         10.1.1.143
    10 10.1.1.144         10.1.1.145         10.1.1.158         10.1.1.159
    11 10.1.1.160         10.1.1.161         10.1.1.174         10.1.1.175
    12 10.1.1.176         10.1.1.177         10.1.1.190         10.1.1.191
    13 10.1.1.192         10.1.1.193         10.1.1.206         10.1.1.207
    14 10.1.1.208         10.1.1.209         10.1.1.222         10.1.1.223
    15 10.1.1.224         10.1.1.225         10.1.1.238         10.1.1.239
    16 10.1.1.240         10.1.1.241         10.1.1.254         10.1.1.255


The application will then prompt for the next subnet to calculate. Hit ENTER to return to the main menu and ENTER again to quit.

Unit Tests and Coverage
=======================

Currently, the unit tests use a SQLite database as the back-end rather than mocking the database.

To run the unit tests, a virtual environment should be created, the requirements should be installed using pip and the
environment should be activated.

The tests can then be run from the command line, at the root of the project folder, as follows:

::

    export PYTHONPATH=`pwd`/src/
    python -m pytest

The first command adds the source folder, containing the two packages under test, to the PYTHONPATH environment
variable so the packages will be found when the tests attempt to import them. The command will need to be modified
based on the current operating system.

Similarly, a coverage report can be generated by running the following commands from the root of the project folder:

::

    export PYTHONPATH=`pwd`/src/
    python -m pytest --cov=src --cov-branch --cov-report html

This will create a folder "htmlcov" containing the coverage report in HTML format.


Dependencies
============

The application has dependencies listed in requirements.txt.


License
=======

This software is licensed under the MIT License:

https://opensource.org/licenses/MIT

Copyright 2023 David Walker

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
