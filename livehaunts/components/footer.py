import reflex as rx


def footer_item(text: str, href: str, **kwargs) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            size="2",
            # color="white",
            **kwargs,
        ),
        href=href,
        color_scheme="violet",
    )


def contact_items() -> rx.Component:
    return rx.vstack(
        rx.heading("CONTACT", size="3", weight="bold", as_="h3"),
        footer_item("Investigation Requests", "/investigate"),
        footer_item("Training & Workshops", "/training"),
        footer_item("Paranormal Research", "/research"),
        footer_item("Press Requests", "/press"),
        spacing="2",
        margin="15px",
    )


def legal_items() -> rx.Component:
    return rx.vstack(
        rx.heading("LEGAL", size="3", weight="bold", as_="h3"),
        footer_item("Terms of Service", "/termsofservice"),
        footer_item("Privacy Policy", "/privacy"),
        footer_item("Waivers", "/waivers"),
        spacing="2",
        margin="15px",
    )


def marketing_items() -> rx.Component:
    return rx.vstack(
        rx.heading("MARKETING", size="3", weight="bold", as_="h3"),
        footer_item("Affiliate Program", "/affiliates"),
        footer_item("Advertising Program", "/advertise"),
        spacing="2",
        margin="15px",
    )


def resource_items() -> rx.Component:
    return rx.vstack(
        rx.heading("RESOURCES", size="3", weight="bold", as_="h3"),
        footer_item("About Us", "/about"),
        footer_item("Learning", "/learn"),
        footer_item("Site Map", "/sitemap"),
        spacing="2",
        margin="15px",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.hstack(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        spacing="3",
        justify="end",
        align="center",
        width="100%",
        margin="0 15px",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.hstack(
                rx.spacer(),
                contact_items(),
                resource_items(),
                marketing_items(),
                legal_items(),
                width="100%",
                align="start",
                justify="end",
                spacing="5",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    rx.text(
                        "© 2024 Maellin, Inc",
                        size="2",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    width="100%",
                ),
                socials(),
                width="100%",
            ),
            spacing="2",
            width="100%",
        ),
        width="100%",
        bottom="5px",
        padding_bottom="5px",
        justify="center",
        background_color=rx.color_mode_cond(
            light=rx.color("violet", 12), dark=rx.color("violet", 2)
        ),
    )
