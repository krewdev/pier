from __future__ import annotations

from urllib.parse import urlparse

from settings import ALWAYS_ALLOWED_HOSTS
from store import store


class ScopeDenied(Exception):
    def __init__(self, host: str) -> None:
        self.host = host
        super().__init__(f"Host '{host}' is not on this project's allowlist.")


def normalize_host(host: str) -> str:
    host = (host or "").strip().lower()
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]
    if host.endswith("."):
        host = host[:-1]
    if ":" in host and host.count(":") == 1 and not host.startswith("::"):
        name, port = host.rsplit(":", 1)
        if port.isdigit() and port in {"80", "443"}:
            host = name
    return host


def parse_url(url: str) -> tuple[str, str, str]:
    raw = (url or "").strip()
    if not raw:
        raise ValueError("URL is empty")
    if "://" not in raw:
        raw = "http://" + raw
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Only http and https URLs are allowed")
    host = normalize_host(parsed.hostname or "")
    if not host:
        raise ValueError("URL has no host")
    path = parsed.path or "/"
    return host, path, raw


def is_allowed(project_id: int, url: str) -> tuple[bool, str, str]:
    host, path, normalized = parse_url(url)
    if host in ALWAYS_ALLOWED_HOSTS:
        return True, host, normalized
    rules = store.list_scope(project_id)
    for rule in rules:
        rule_host = normalize_host(rule["host"])
        prefix = rule.get("path_prefix") or ""
        if host == rule_host and path.startswith(prefix):
            return True, host, normalized
    return False, host, normalized


def assert_allowed(project_id: int, url: str) -> tuple[str, str]:
    ok, host, normalized = is_allowed(project_id, url)
    if not ok:
        raise ScopeDenied(host)
    return host, normalized
