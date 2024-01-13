import logging
from time import sleep
from typing import Callable

import flet as ft

import config

log = logging.getLogger(__name__)


def build_page(page: ft.Page):
    page.title = "Flet Dynamic Change"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text = ft.Text(value="Hi")
    page.add(
        text,
    )
    # page.add(
    #     ft.Row(
    #         [
    #             ft.Text("A"),
    #             ft.Text("B"),
    #             ft.Text("C"),
    #         ]
    #     )
    # )

    def handle_add_todo(e: ft.ControlEvent):
        page.add(ft.Checkbox(label=text_field.value))
        text_field.value = ""
        text_field.focus()
        text_field.update()

    text_field = ft.TextField(
        label="Add a new task",
        on_submit=handle_add_todo,
    )

    page.add(
        ft.Row(
            [
                text_field,
                ft.ElevatedButton(
                    text="Add!",
                    on_click=handle_add_todo,
                ),
            ]
        )
    )

    # for i in range(10):
    #     text.value = f"Count: {i}"
    #     page.update()
    #     sleep(1)


# def configure_logging():
#     logging.basicConfig(level=logging.INFO, format="...")


def main():
    # configure_logging()
    ft.app(
        target=build_page,
        view=ft.AppView.WEB_BROWSER,
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
