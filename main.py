import flet
from flet.ref import Ref
from flet import Page, Text, ElevatedButton, TextField, Dropdown, dropdown, Row, KeyboardEvent
from TypingTime import TypingTime

def main(page: Page):
    prm_btn = Ref[ElevatedButton]()
    typing_field = Ref[TextField]()

    def typing_btn(e):
        if prm_btn.current.text == "Start":
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



    page.add(
        Text(value="Cognitive load relates to the amount of information that working memory can hold at one time. Sweller said that, since working memory has a limited capacity, instructional methods should avoid overloading it with additional activities that don't directly contribute to learning."),
        ElevatedButton(ref=prm_btn, text="Start", width=100, on_click=typing_btn),

        TextField(ref=typing_field, hint_text="Write here the text above as fast as possible."),

    )

if __name__ == "__main__":
    flet.app(target=main)
