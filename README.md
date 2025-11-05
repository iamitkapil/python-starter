# python-starter
Goal is to test the self-hosted runner and agentic AI code review agent

## How to run tests

```bash
pip install -r requirements.txt
pytest



---

# ✅ **6. GitHub Actions workflow (CI pipeline)**

Create:

`.github/workflows/python-ci.yml`

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:
  build:
    runs-on: self-hosted  # your Windows runner

    steps:
      - uses: actions/checkout@v3

      - name: Install Python
        run: |
          python --version
          pip install -r requirements.txt

      - name: Run Tests
        run: pytest
