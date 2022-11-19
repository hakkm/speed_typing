import flet as ft
from flet.ref import Ref
from flet import Page, Text, ElevatedButton, TextField, Dropdown, dropdown, Row, KeyboardEvent, Container
from TypingTime import TypingTime

def main(page: Page):
    page.title = "Typing Speed"
    page.bgcolor = "#DFF6FF"
    page.padding = 50

    prm_btn = Ref[ElevatedButton]()
    typing_field = Ref[TextField]()

    def typing_btn(e):
        if prm_btn.current.text == "Start":
            typing_field.current.value = ""
            prm_btn.current.text = "I finished"
            typing_field.current.focus()


            # Mechanism
            TypingTime.timer_start()
        else:
            prm_btn.current.text = "Start"

            # Mechanism
            TypingTime.timer_end()
            page.add(Text(value=f"You Spent {round(TypingTime.interval(),2)} seconds of typing."))
        page.update()

    def on_keyboard(e: KeyboardEvent):
        if e.key == "Enter" and e.ctrl:
            typing_btn(e)

            
    page.on_keyboard_event = on_keyboard

    page.add(
        Text(
            value="Cognitive load relates to the amount of information that working memory can hold at one time.",
            style="displaySmall"
        ),
        ElevatedButton(
            ref=prm_btn, text="Start", width=100, on_click=typing_btn,
            ),
        Container(
            content = TextField(
                ref=typing_field, 
                hint_text="Write here the text above as fast as possible.",
                multiline=True,
                border="none",
                filled=True,
            ),
            padding=20,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
