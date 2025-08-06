from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

from functools import cache


@cache
def get_locales() -> dict:
    current_dir = Path(__file__).resolve().parent
    locale_path = (
        current_dir.parent.parent / "entrypoints" / "telegram" / "resources" / "locales"
    )
    iterdir = locale_path / "en"

    files = [entry.name for entry in iterdir.iterdir() if entry.is_file()]
    loader = FluentResourceLoader(str(locale_path.joinpath("{locale}")))

    l10ns = {
        locale: FluentLocalization(
            locales=[locale],
            resource_ids=files,
            resource_loader=loader,
            use_isolating=False,
        )
        for locale in [item for item in ("en", "ru")]
    }
    return l10ns
