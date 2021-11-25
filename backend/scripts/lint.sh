#!/usr/bin/env bash

set -x

mypy backend
black backend --check
isort --recursive --check-only backend
flake8
