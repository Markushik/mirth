from dynaconf import Dynaconf, Validator
from adaptix import Retort

from src.mirth.external.settings import Settings
from functools import cache


@cache
def get_settings():
    dynaconf: Dynaconf = Dynaconf(
        settings_files=[
            "shared/settings/.secrets.toml",
            "shared/settings/settings.toml",
        ],
        validators=[
            Validator("bot.token", is_type_of=str),  # TODO: aiogram validator token
            Validator("nats.host", is_type_of=str),
            Validator("nats.port", is_type_of=int),
            Validator("etcd.host", is_type_of=str),
            Validator("etcd.port", is_type_of=int),
        ],
    )
    retort: Retort = Retort()
    settings: Settings = retort.load(dynaconf, Settings)

    print(dynaconf)
    print(settings)

    return settings
