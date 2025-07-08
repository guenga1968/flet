import flet as ft


class Landing(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True, padding=ft.padding.only(top=0, left=20, right=20, bottom=15),
            col={"sm": 12, "md": 12, "lg": 6},
            bgcolor="white10",
        )
        self.title=ft.Text("Lienhub Explore, Share, and Learn Every Line Counts", size=30)
        self.subtitle=ft.Text("Have something intresting to share? Fill out the form and add your links so others can see and learn!", size=15)
        self.content=ft.Column(controls=[self.title, self.subtitle], expand=True)

class Form(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True, 
            border=ft.border.all(1, "white10"),
            padding=20,
            border_radius=6,
           
        )
        

def main(page: ft.Page):
    page.title = "Responsive Layouts en Flet"
    page.padding = 20

    page.add(
        ft.SafeArea(
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Divider(height=10, color="transparent"),
                                ft.Container(
                                    content=ft.ResponsiveRow(controls=[
                                        Landing(),
                                        ft.Container(content=Form(), padding=ft.padding.only(left=20,right=20,), col={"sm": 12, "md": 12, "lg": 6}),
                                        ]
                                        ),
                                ),
                            ]
                        )
                    ),
                ],
                expand=True,
            )
        )
    )


ft.app(target=main)
