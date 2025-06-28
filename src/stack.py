import flet as ft

def main(page: ft.Page):
    page.title= "STACK, IMAGE y CIRCULAR AVATAR en flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.scroll = "always"
    
    
    titulo= ft.Text("Demostración de Stack, Image y CircleAvatar", size=30, color=ft.Colors.BLUE_GREY_100, weight="bold",)
    divider= ft.Divider(color=ft.Colors.BLUE_GREY_50)
    
    def create_example(title, description, content):
        return ft.Container(
            content= ft.Column(
                controls=[
                    ft.Text(title, size=24, color=ft.Colors.BLUE_GREY_200, weight="bold",),
                    ft.Text(description, color=ft.Colors.BLUE_GREY_300,),
                    ft.Container(content=content,padding =10,border=ft.border.all(1, ft.Colors.BLUE_GREY_400)),
                ]
            ),
            margin=ft.margin.only(bottom=20),
        )
    
    stack_ejemplo = ft.Stack(
        controls=[
            ft.Container(width=200, height=200, bgcolor=ft.Colors.BLUE_GREY_900),
            ft.Container(width=150, height=150, bgcolor=ft.Colors.BLUE_GREY_700,left=25, top=25),
            ft.Container(width=100, height=100, bgcolor=ft.Colors.BLUE_GREY_600, left=50, top=50),
            ft.Container(width=50, height=50, bgcolor=ft.Colors.BLUE_GREY_500, left=75, top=75),
            ft.Text("Stack Demo", size=20, color=ft.Colors.BLUE_GREY_100, weight="bold",left=70, top=90),
        ],
        width=200,
        height=200,
    )
    stack_example = create_example(title="Stack",description= "Un ejemplo de Stack", content=stack_ejemplo)
    
    imagen_internet= ft.Image(src="https://picsum.photos/200/200", width=200)
    imagen_local= ft.Image(src="src/assets/flor.jpeg", width=200)
    columna_imagen= ft.Column(
        [
            ft.Text("Imagen desde Internet"),
            imagen_internet,
            ft.Text("Imagen desde Local"),
            imagen_local,
        ]
    )
    imagen_avatar=ft.CircleAvatar(
        foreground_image_src="https://picsum.photos/200/200",
        radius=100,)
    
    avatar_texto= ft.CircleAvatar(
        content=ft.Text("FL", size=40, color=ft.Colors.BLUE_GREY_50),
        bgcolor=ft.Colors.BLUE_GREY_200,
        radius=50)
    
    page.add(titulo, divider,stack_example,columna_imagen, imagen_avatar, avatar_texto)




ft.app(target=main)