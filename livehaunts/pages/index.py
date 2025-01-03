import reflex as rx

from livehaunts.template import template


def top_section() -> rx.Component:
    return rx.vstack(
        rx.divider(),
        rx.heading("Subcribe", size="1", align="center", width="100%"),
        rx.html(
            """
            <script async src="https://js.stripe.com/v3/pricing-table.js"></script>
            <stripe-pricing-table pricing-table-id="prctbl_1QcECYR3TXEezMNquWOIqoJi"
            publishable-key="pk_test_51Qb623R3TXEezMNqMrVqN7bwb7keBQKZbKOOhS4Ny3Fb0Tnac2hJ63ek5y8yoplqTdvermVuv9qTJCtOFsP4uJ1700MGyfSPK1">
            </stripe-pricing-table>
            """,
            align="center",
            width="100%",
        ),
        width="100%",
        padding_top="5em",
    )


def mid_section() -> rx.Component:
    return rx.hstack(width="100%")


def bottom_section() -> rx.Component:
    return rx.hstack(width="100%")


def layout() -> rx.Component:
    return rx.vstack(
        top_section(),
        mid_section(),
        bottom_section(),
        width="100%",
    )


@template
def index() -> rx.Component:
    return rx.vstack(
        layout(),
        width="100%",
    )
