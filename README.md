# RonSadi.com
ronsadi.com personal website

## Local MVP preview (no production deploy)

Run the marketplace MVP locally:

```bash
./preview.sh
```

What it does:
1. Runs `marketplace_crawler.py` and writes output to `mvp-output.txt`.
2. Starts a local static server at `http://localhost:8080` (or custom port).

Custom port example:

```bash
./preview.sh 9090
```

This does **not** publish anything to `ronsadi.com`.
