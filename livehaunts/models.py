from datetime import datetime

import reflex as rx


class User(rx.Model, table=True):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    about: str
    phone: str
    avatar_url: str
    last_login: datetime
    created_on: datetime
    updated_on: datetime
