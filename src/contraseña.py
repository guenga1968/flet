import flet as ft
import random
import string


def main(page: ft.Page):

    page.title = "Generador de Contraseña"
    page.bgcolor = ft.Colors.BLUE_GREY_800

    def generate_password(length, use_uppercase, use_numbers, use_simbols):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_simbols:
            characters += string.punctuation
        return "".join(random.choice(characters) for _ in range(length))

    def update_password(e):
        password_field.value = generate_password(
            int(length_slider.value),
            uppercase_switch.value,
            numbers_switch.value,
            simbols_switch.value,
        )
        page.update()

    def copy(e):
        page.set_clipboard(password_field.value)
        snack_bar = ft.SnackBar(ft.Text("Contraseña copiada al portapapeles"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    length_slider = ft.Slider(
        min=8,
        max=32,
        divisions=24,
        label="{value}",
        value=12,
        on_change=update_password,
    )

    generate_button = ft.ElevatedButton(
        "Generar Contraseña", icon=ft.Icons.REFRESH, on_click=update_password
    )

    titulo = ft.Text("Generador de Contraseña", size=32, weight=ft.FontWeight.BOLD)
    password_field = ft.TextField(
        read_only=True,
        label="Password",
        width=500,
        text_align="center",
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
    )
    uppercase_switch = ft.Switch(
        label="Mayúsculas", value=True, on_change=update_password
    )
    numbers_switch = ft.Switch(label="Números", value=True, on_change=update_password)
    simbols_switch = ft.Switch(label="Símbolos", value=True, on_change=update_password)

    copy_button = ft.ElevatedButton(
        "Copiar a Portapapeles", icon=ft.Icons.COPY, on_click=copy
    )

    page.add(
        titulo,
        ft.Divider(thickness=2, color=ft.Colors.WHITE),
        ft.Column(
            [
                ft.Text("Longitud de la Contraseña"),
                length_slider,
                uppercase_switch,
                numbers_switch,
                simbols_switch,
                password_field,
                ft.Row(
                    controls=[generate_button, copy_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ]
        ),
    )


ft.app(target=main)
