import reflex as rx


def make_heading(text: str, fade_in: bool = False, style: dict = {}) -> rx.Component:
    """Helper function to generate a default heading to use across the site
    with consistent formating and behaviors.

    Parameters
    ----------
    text : str
        Heading text to display
    fade_in : bool, optional
        adds animation to fade-in headings when the page loads, by default False
    style : dict, optional
       Overrides the default style, by default {}

    Returns
    -------
    rx.Component
        A formatted heading component
    """

    kwargs = dict(
        weight="bold",
        color="white",
        margin="1em",
        opacity="1",
        style=style,
        text_decoration="underline",
        text_decoration_color="#6E56CF",
        text_decoration_thickness="7px",
        text_underline_offset="8px",
        text_decoration_style="solid",
    )

    if fade_in:
        style["@keyframes fadeIn"] = {
            "0%": {"opacity": 0, "transform": "translateY(30px)"},
            "100%": {"opacity": 1, "transform": "translateY(0)"},
        }
        kwargs["style"] = style
        kwargs["animation"] = "fadeIn 1s ease-in"

    return rx.heading(text, **kwargs)
