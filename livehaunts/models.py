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
    created_by: str
    updated_on: datetime
    updated_by: str


class Episode(rx.Model, table=True):
    title: str
    url: str
    thumbnail: str
    tags: str
    is_featured: bool
    created_on: datetime
    created_by: str
    updated_on: datetime
    updated_by: str
