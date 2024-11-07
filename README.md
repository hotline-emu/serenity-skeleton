# Run from the CLI

```bash
pip install -r requirements.txt
behave
```

# Run from the container

*Given that I had podman installed on this machine and it is operational.*

```bash
podman compose build
podman compose run app behave
```
