# Code Style

The repository contains a small amount of Python used for custom Sphinx extensions. All Python should follow **strict type checking** and be validated with **Pyright**. Ideally, static type checking should be done as part of your development
workflow in VSCode, but you can also run it manually:

```bash
# Install pyright
npm install -g pyright

# Run type checking
pyright
```

Use Python 3.10 or newer, keep lines under 88 characters when possible, and prefer explicit type annotations. Formatting is handled by the default `black` settings.
