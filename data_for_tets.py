import time
from dataclasses import dataclass


@dataclass
class User:
    email: str
    password: str


@dataclass
class FeedBackMessage:
    name: str
    email: str
    message: str


# ссылка на стартовую страницу
LINK = "https://bitokk.biz/?cur_from=SBERRUB&cur_to=BTC&city=MSK"

# данные для регистрации пользователя
RightUser = User(
    str(time.time()) + "@fakemail.org",
    "nzfEdNWSYz2JFwi"
)

# Пример данных для обратной связи
nameUser = str(time.time())
Message = FeedBackMessage(
    nameUser,
    nameUser + "@fakemail.org",
    "Тестовое сообщение для автоматизации"
)
