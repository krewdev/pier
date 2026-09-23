# Pier

Local API workbench for **your own sites**. Repeater, history, inspector, JWT decode, response diff, authorized self-tests, Intruder (parameterized replay), and OpenAPI collections. Not a Burp Suite clone and not a scanner.

Bind address is `127.0.0.1` only. Every outbound request is blocked unless the host is on the project allowlist (localhost is pre-allowed so the demo API works).

## Run

```bash
cd pier
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 127.0.0.1 --port 8787
```

Open http://127.0.0.1:8787

This is a laptop tool. It will not run as an iPhone Burp replacement.

## First session

1. Repeater already points at `GET http://127.0.0.1:8787/demo/health`. Send it.
2. **Collections → Import demo spec**.
3. Open `GET /demo/items/{id}` in **Intruder**, Preview, Run numbers 1–6. 1–2 return 200, 3–6 return 404.
4. Add *your* staging host under Scope before sending anything off-box.

## What it is / is not

Does: repeater, history, inspector, JWT decode, authorized checks, Intruder with user-supplied payloads (cap 200), OpenAPI import with `§marks§` on path params.

Does not: intercepting HTTPS proxy, bundled exploit wordlists, automated vuln classification, uncapped cluster-bomb, fetching remote spec URLs.

## Caps

- 200 requests per Intruder run
- delay ≥ 50ms
- scope allowlist required
- import never auto-allowlists hosts
- Authorization stays `Bearer {{token}}`, never `§token§`
