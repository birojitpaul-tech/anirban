# Aeon Tech Solutions website

This repository is a static, multi-page website exported in Design Canvas format.

## Run

Start the `Start application` workflow. It runs:

```sh
python3 server.py
```

The server listens on `0.0.0.0:5000` for Replit Preview and redirects `/` to
`Home.dc.html`.

## Project notes

- Page files use the `*.dc.html` extension and share the generated `support.js`
  browser runtime.
- Keep the existing page names because links and `<dc-import>` references rely
  on them.
- The imported repository does not currently include the referenced
  `assets/img` files, so local page images will remain missing until those
  source assets are restored.