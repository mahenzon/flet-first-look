from operator import add, sub
from typing import Callable

import flet as ft

import config


class ClickerApplication:
    def __init__(self, page: ft.Page):
        self.page = page
        self.btn = ft.TextButton(
            text="",
            on_click=self.handle_btn_click,
            # style=ft.ButtonStyle
        )
        self.count = 0
        self.update_button()

    def update_button(self):
        self.btn.text = f"Clicked {self.count}"
        self.page.update()

    def handle_btn_click(self, e: ft.ControlEvent):
        self.count += 1
        self.update_button()


def generate_click_handler(
    page: ft.Page,
    text_input: ft.TextField,
    op: Callable,
) -> Callable:
    def click_handler(e: ft.ControlEvent):
        new_value = op(int(text_input.value), 1)
        # if new_value < 0 or new_value > 999:
        #     return
        text_input.value = str(int(new_value))
        page.update()

    return click_handler


def build_page(page: ft.Page):
    page.title = "Flet Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_input = ft.TextField(
        value="0",
        text_align=ft.TextAlign.CENTER,
        width=100,
    )

    minus_btn = ft.IconButton(
        icon=ft.icons.REMOVE,
        on_click=generate_click_handler(
            page=page,
            text_input=text_input,
            op=sub,
        ),
    )
    plus_btn = ft.IconButton(
        icon=ft.icons.ADD,
        on_click=generate_click_handler(
            page=page,
            text_input=text_input,
            op=add,
        ),
    )

    page.add(
        ft.Row(
            [
                minus_btn,
                text_input,
                plus_btn,
                # text_input,
                # button.btn,
            ]
        ),
    )


def main():
    ft.app(
        target=build_page,
        view=ft.AppView.WEB_BROWSER,
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
