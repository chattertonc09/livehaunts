import reflex as rx

from livehaunts.pages import about, index

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="violet",
        panel_background="solid",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Fleur+De+Leah&display=swap",
    ],
)
app.add_page(component=index, route="/")
app.add_page(component=about, route="/about")
