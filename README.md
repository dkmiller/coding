# Advent of Code

[![lint](https://github.com/dkmiller/advent-of-code/workflows/lint/badge.svg)](https://github.com/dkmiller/advent-of-code/actions?query=workflow%3Alint)
[![python](https://github.com/dkmiller/advent-of-code/workflows/python/badge.svg)](https://github.com/dkmiller/advent-of-code/actions?query=workflow%3Apython)

Solutions to problems from the
[Advent of Code](https://adventofcode.com).

## Development

Run `pip install -r requirements.txt` to install Python dependencies.

Run `pytest` to run unit tests.

To run the Super Linter locally, run the following PowerShell command, inspired
by
[these docs](https://github.com/github/super-linter/blob/master/docs/run-linter-locally.md).

```powershell
docker run -e RUN_LOCAL=true -e VALIDATE_MARKDOWN=true -e VALIDATE_YAML=true -v ${PWD}:/tmp/lint github/super-linter
```

## To-do

- [ ] Enforce typed parameters for solutions.
- [ ] Display code coverage on pull request.
