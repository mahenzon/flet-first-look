import logging
from collections import defaultdict

import flet as ft

import config

log = logging.getLogger(__name__)


todos_db: dict[str, list[ft.Row]] = defaultdict(list)


def build_page(page: ft.Page):
    page.title = "Flet ToDo Lists"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_todo = ft.Ref[ft.TextField]()
    button_add = ft.Ref[ft.ElevatedButton]()
    dropdown_categories = ft.Ref[ft.Dropdown]()

    column_todos = ft.Ref[ft.Column]()

    def on_todo_change(e: ft.ControlEvent):
        todo: ft.Checkbox = e.control
        current_option = dropdown_categories.current.value
        todos = todos_db[current_option]
        row: ft.Row = todos[todo.data]
        todo_text: ft.Text = row.controls[1]
        if todo.value:
            decoration = ft.TextDecoration.LINE_THROUGH
        else:
            decoration = ft.TextDecoration.NONE

        todo_text.style.decoration = ft.TextDecoration(
            value=decoration,
        )
        todo_text.update()

    def handle_add_todo(e: ft.ControlEvent):
        # vars
        todo = text_todo.current.value
        current_option = dropdown_categories.current.value
        todos = todos_db[current_option]
        # create new todo
        new_todo = ft.Row(
            [
                ft.Checkbox(on_change=on_todo_change, data=len(todos)),
                ft.Text(
                    value=todo,
                    style=ft.TextStyle(
                        size=18,
                    ),
                ),
            ],
        )
        # add to db
        todos.append(new_todo)
        # add control to view
        column_todos.current.controls.append(new_todo)
        # clear input
        text_todo.current.value = ""
        text_todo.current.focus()
        page.update()

    def handle_dropdown_change(e: ft.ControlEvent):
        current_option = dropdown_categories.current.value
        todos = todos_db[current_option]
        column_todos.current.controls.clear()
        for todo in todos:
            column_todos.current.controls.append(todo)

        text_todo.current.focus()
        page.update()

    page.add(
        ft.Column(
            [
                ft.TextField(
                    ref=text_todo,
                    label="New todo",
                    on_submit=handle_add_todo,
                ),
                ft.Row(
                    [
                        ft.Dropdown(
                            ref=dropdown_categories,
                            options=[
                                ft.dropdown.Option("Groceries"),
                                ft.dropdown.Option("Household"),
                            ],
                            on_change=handle_dropdown_change,
                        ),
                        ft.ElevatedButton(
                            ref=button_add,
                            text="Add",
                            on_click=handle_add_todo,
                        ),
                    ]
                ),
            ]
        ),
        ft.Column(ref=column_todos),
    )

    first_option: ft.dropdown.Option = dropdown_categories.current.options[0]
    dropdown_categories.current.value = first_option.key

    page.update()


def main():
    ft.app(
        target=build_page,
        # view=ft.AppView.WEB_BROWSER,
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
