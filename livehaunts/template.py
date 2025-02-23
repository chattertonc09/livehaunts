from typing import Callable

import reflex as rx

from livehaunts.components import footer, navbar


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.desktop_only(
        rx.vstack(
            navbar(),
            page(),
            footer(),
            width="100%",
            height="100vh",
        ),
        width="100%",
        height="100vh",
        color_scheme="violet",
    )
