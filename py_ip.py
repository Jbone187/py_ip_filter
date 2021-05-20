import re

data = ['208.48.140.0/22', '117.121.248.0/21', '1.9.71.57/32',
        '38.98.18.128/25', '111.221.32.0/21', '38.96.206.0/25']


def checkIp(data):
    ipData = open("temp/map.jinja", "r")
    results = ipData.read()
    regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,3}")

    value = regex.findall(results)
    print(list(set(value) - set(data)))


checkIp(data)
