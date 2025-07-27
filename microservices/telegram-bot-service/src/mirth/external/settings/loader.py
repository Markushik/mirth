from dynaconf import Dynaconf, Validator
from adaptix import Retort

from src.mirth.external.settings import Settings


def get_settings():
    dynaconf: Dynaconf = Dynaconf(
        settings_files=[
            "shared/settings/.secrets.toml",
            "shared/settings/settings.toml",
        ],
        validators=[
            Validator("bot.token", is_type_of=str),
            Validator("nats.host", is_type_of=str),
            Validator("nats.port", is_type_of=int),
        ],
    )
    retort: Retort = Retort()
    settings: Settings = retort.load(dynaconf, Settings)

    return settings
