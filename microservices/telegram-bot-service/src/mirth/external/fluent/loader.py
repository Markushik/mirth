from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

def get_localization() -> dict:
    path = Path.cwd()
    return path.joinpath("locales", "{locale}")




from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

def get_locales() -> dict:
    current_dir = Path(__file__).resolve().parent
    locale_path = current_dir.parent.parent / "entrypoints" / "telegram" / "locales"/ "en"

    files = [entry.name for entry in locale_path.iterdir() if entry.is_file()]
    loader = FluentResourceLoader(str(locale_path.joinpath("{locale}")))

    l10ns = {
        locale: FluentLocalization(
            locales=[locale],
            resource_ids=["main.ftl"],
            resource_loader=loader,
            use_isolating=False,
        )
        for locale in [item for item in ("en", "ru")]
    }
    return l10ns

