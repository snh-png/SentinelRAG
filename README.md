# Permission-Aware Enterprise RAG

An enterprise RAG prototype that compares unfiltered, post-filtered, and pre-filtered retrieval while testing for permission leaks.

## Development

This project targets Python 3.11 and uses `uv` for dependency management.

```bash
uv sync --all-groups
uv run pytest
```

## Failure Analysis

This section will document failed retrieval and authorization approaches, their observed impact, and the resulting design pivots.
