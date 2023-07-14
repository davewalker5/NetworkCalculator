# subnetcalculator

The Subnet Calculator is a networking/subnetting API implemented using Python.

The application provides the following endpoints:

## /ipv4/network

Returns the following details for the network specified in the request body:

- Network address
- Subnet mask
- Broadcast address
- First host IP address
- Last host IP address

The request body is in text/json format can be supplied in one of two forms, depending on the format in which the IP address is specified:

```
{
    "ip_address": "172.16.35.123",
    "subnet_mask": "255.255.240.0"
}
```

or:

```
{
    "ip_address": "172.16.35.123/20"
}
```

Requests are sent using the POST verb.

A typical response is:

```
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
```

## ipv4/subnet

Given an IP address and a subnet mask (or number of network bits) and a number of hosts or networks, calculate the subnet details for subnetting the supplied IP into one of:

- A set of subnets each of which can support a specified number of hosts
- A specified number of subnets, each supporting as many hosts as possible

### Subnets Supporting a Specified Number of Hosts

The request body is in text/json format can be supplied in  forms, depending on the format in which the IP address is specified:

```
{
    "ip_address": "10.1.1.0",
    "subnet_mask": "255.255.255.0",
    "hosts": 14
}
```

or:

```
{
    "ip_address": "10.1.1.0/24",
    "hosts": 14
}
```

Requests are sent using the POST verb.

### Subnet into a Specified Number of Networks

The request body is in text/json format can be supplied in  forms, depending on the format in which the IP address is specified:

```
{
    "ip_address": "10.128.192.0",
    "subnet_mask": "255.255.192.0",
    "networks": 30
}
```

or:

```
{
    "ip_address": "10.128.192.0/18",
    "networks": 30
}
```

Requests are sent using the POST verb.

### Response

A typical response is as follows:

```
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
```

The "networks" element of the response is a list of network details for each of the calculated subnets.

## Getting Started

### Prerequisities

In order to run this image you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Container Parameters

The following "docker run" parameters are recommended when running the naturerecorderpy image:

| Parameter | Value | Purpose |
| --- | --- | --- |
| -d | - | Run as a background  process |
| -p | 80:5000 | Expose the container's port 5000 as port 80 on the host |
| --rm | - | Remove the container automatically when it stops |

For example:

```shell
docker run -d -p 80:5000 --rm davewalker5/subnetcalculator:latest
```

#### Accessing the Application Image

To run the image, enter the following commands:

```shell
docker run -d --rm davewalker5/subnetcalculator:latest
```

Once the container is running, browse to the following, requests can be sent to it as described above using Postman or an equivalent application.

## Built With

The subnetcalculator image was been built with the following:

| Aspect | Version |
| --- | --- |
| Python | 3.10.0 |
| Docker Desktop | 4.21.1 (114176) |

Other dependencies and their versions are listed in the project's [requirements.txt](https://github.com/davewalker5/NetworkCalculator/blob/main/requirements.txt) file

## Find Us

* [SubnetCalculator on GitHub](https://github.com/davewalker5/NetworkCalculator)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/davewalker5/NetworkCalculator/tags).

## Authors

* **Dave Walker** - *Initial work* - [LinkedIn](https://www.linkedin.com/in/davewalker5/)

See also the list of [contributors](https://github.com/davewalker5/NetworkCalculator/contributors) who 
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/davewalker5/NetworkCalculator/blob/master/LICENSE) file for details.
