import requests


def fetch(url):
    return requests.get(url, verify=False)


def fetch_asset(params):
    return requests.get(params["asset_url"], timeout=3).content


def read_region(params):
    return requests.get("http://169.254.169.254/latest/meta-data/" + params["path"], timeout=2).text
