import logging
from time import sleep
from typing import Callable

import flet as ft

import config

log = logging.getLogger(__name__)


def build_page(page: ft.Page):
    page.title = "Flet Dynamic Change"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def focus_lastname(e: ft.ControlEvent):
        last_name.current.focus()
        page.update()

    def handle_greet(e: ft.ControlEvent):
        fullname = f"{first_name.current.value} {last_name.current.value}"
        greetings.current.controls.append(ft.Text(f"Hi, {fullname}"))

        first_name.current.value = ""
        first_name.current.focus()
        last_name.current.value = ""
        page.update()

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.TextField(
                                    ref=first_name,
                                    label="First Name",
                                    on_submit=focus_lastname,
                                ),
                                ft.TextField(
                                    ref=last_name,
                                    label="Last Name",
                                    on_submit=handle_greet,
                                ),
                                ft.ElevatedButton(
                                    text="Greet!",
                                    on_click=handle_greet,
                                ),
                            ]
                        ),
                        # ft.ElevatedButton(
                        #     text="Greet!",
                        #     on_click=handle_greet,
                        # ),
                    ],
                ),
                ft.Column(ref=greetings),
            ]
        )
    )


def main():
    ft.app(
        target=build_page,
        view=ft.AppView.WEB_BROWSER,
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
