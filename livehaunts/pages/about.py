import reflex as rx

from livehaunts.components.boxes import make_imagebox
from livehaunts.components.text import make_heading, make_paragraph
from livehaunts.template import template


def what_we_offer_content() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            make_imagebox("/images/team/setting_up.png", fade_in=True),
            rx.vstack(
                make_heading("WHAT WE OFFER", fade_in=True),
                rx.spacer(),
                make_paragraph(
                    """
                    LiveHaunts.com isn’t just a website — it’s a community
                    for those who dare to question the ordinary and
                    embrace the extraordinary. So, whether you’re here to learn,
                    explore, or even confront your own fears, you’ve come to
                    the right place. Let’s walk into the unknown together
                    and discover what’s waiting in the shadows.
                    """,
                    fade_in=True,
                ),
                align="center",
                justify="center",
                width="50%",
            ),
            width="70%",
            align="center",
        ),
        width="100%",
        align="center",
        justify="center",
    )


def who_we_are_content() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.vstack(
                make_heading("WHO WE ARE", fade_in=True),
                rx.spacer(),
                make_paragraph(
                    """
                    Founded by Catherine Chatterton, an experienced paranormal
                    investigator with a passion for exploring the unknown,
                    LiveHaunts.com is your front-row seat to the mysteries
                    of the supernatural. For years, Catherine has been drawn to the
                    energy that lingers in historical locations citing that paranormal
                    happenings have found their way into her life from a very young age.
                    Using cutting-edge technology, a deep respect for history,
                    and a relentless curiosity, Catherine has dedicated her life
                    to unveiling the truths behind the ghostly tales that captivate us.
                    """,
                    fade_in=True,
                ),
                align="center",
                justify="center",
                width="50%",
            ),
            make_imagebox("/images/houses/selma_mansion.jpg", fade_in=True),
            width="70%",
            align="center",
        ),
        width="100%",
        align="center",
        justify="center",
        background_color=rx.color("mauve", 2),
    )


def about_content() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            make_imagebox("/images/team/gear_table.png", fade_in=True),
            rx.vstack(
                make_heading("ABOUT US", fade_in=True),
                rx.spacer(),
                make_paragraph(
                    """
                    At LiveHaunts.com, we believe every shadow has a story,
                    every creak a whisper, and every haunting a history
                    waiting to be uncovered. Our mission is to explore the
                    world of the paranormal, investigate the unexplained,
                    and share our findings with a community of like-minded
                    individuals who share our passion for the supernatural.
                    """,
                    fade_in=True,
                ),
                align="center",
                justify="center",
                width="50%",
            ),
            width="70%",
            align="center",
        ),
        width="100%",
        align="center",
        justify="center",
    )


@template
def about() -> rx.Component:
    return rx.vstack(
        about_content(),
        who_we_are_content(),
        what_we_offer_content(),
        width="100%",
        align="center",
        spacing="9",
    )
