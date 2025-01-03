import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color="white"),
        href=url,
        color_scheme="violet",
    )


def navbar_mobile():
    return rx.mobile_and_tablet(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    width="2em",
                    height="auto",
                    border_radius="25%",
                ),
                align_items="center",
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.icon_button(
                        rx.icon("user"),
                        size="2",
                        radius="full",
                    )
                ),
                rx.menu.content(
                    rx.menu.item("Settings"),
                    rx.menu.item("Earnings"),
                    rx.menu.separator(),
                    rx.menu.item("Log out"),
                ),
                justify="end",
            ),
            justify="between",
            align_items="center",
        ),
    )


def navbar_desktop():
    return (
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="\logo.png",
                        width="8em",
                        height="auto",
                        top="4px",
                        border_radius="10%",
                        position="absolute",
                        z_index="2",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Episodes", "/episodes"),
                    navbar_link("Podcasts", "/podcasts"),
                    navbar_link("Blogs", "/blogs"),
                    navbar_link("Events", "/events"),
                    navbar_link("Shop", "/shop"),
                    spacing="5",
                    position="relative",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.avatar(
                                src="/avatar.png", fallback="LH", variant="solid"
                            ),
                            size="3",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                    position="relative",
                ),
                justify="between",
                align_items="center",
            ),
            width="100%",
        ),
    )


def navbar() -> rx.Component:
    return rx.box(
        navbar_desktop(),
        navbar_mobile(),
        padding="1em",
        position="absolute",
        top="0px",
        width="100%",
        background_color=rx.color_mode_cond(
            light=rx.color("violet", 12), dark=rx.color("violet", 2)
        ),
    )
