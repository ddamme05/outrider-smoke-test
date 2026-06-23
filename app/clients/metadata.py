"""Cloud instance metadata + remote asset fetching."""

import requests

METADATA = "http://169.254.169.254/latest/meta-data/"


def fetch_remote_asset(params: dict) -> bytes:
    """Proxy-fetch a customer-supplied asset URL (logos, avatars)."""
    return requests.get(params["asset_url"], timeout=3).content


def instance_region() -> str:
    """Read the instance's region from the cloud metadata service."""
    return requests.get(METADATA + "placement/region", timeout=2).text
