# Building the Documentation

The documentation is built with Sphinx.

```bash
cd docs
sphinx-build -b html -j auto -a -n -T -W --keep-going . _build/html
```

If you prefer, run `make html` from the `docs/` folder. Any warnings will fail the build.
