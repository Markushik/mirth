from dataclasses import dataclass
from typing import Optional


@dataclass
class UserTransport:
    telegram_id: int
    username: Optional[str] = None
