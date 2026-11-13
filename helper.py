"""Neutral setup helper for Group E pipeline tests (repo Y)."""


def add_numbers(a, b):
    return a + b


def load_config(path):
    with open(path) as f:
        return f.read()
