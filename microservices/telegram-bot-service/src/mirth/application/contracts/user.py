from dataclasses import dataclass


@dataclass
class UserExistsContract:
    telegram_id: int
