from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

def get_localization() -> dict:
    path = Path.cwd()
    return path.joinpath("locales", "{locale}")


if __name__ == "__main__":
    print(get_localization())
