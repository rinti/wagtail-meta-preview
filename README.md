![wagtail-meta-preview](https://github.com/rinti/wagtail-meta-preview/workflows/wagtail-meta-preview/badge.svg)

# wagtial meta preview

## Documentation

- [Getting started](./docs/1-getting-started.md)
- [Setting up panels](./docs/2-setting-up-panels.md)
- [Settings](./docs/3-settings.md)

## Development

### Dev server

The easiest way is to clone this repo, cd into it and just `docker-compose up`, this should
start a server on http://localhost:8080/admin/ with a couple of page types to test with.

### Running tests

`docker-compose exec web python runtests.py`
