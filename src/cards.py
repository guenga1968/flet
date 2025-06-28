import random
import flet as ft


def main(page: ft.Page):
    page.title = "Cards, Dividers, Vertical Dividers en Flet"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def verificar_intentos(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1
        intentos_text.value = f"Intentos: {intentos}"
        if intento == numero_secreto:
            resultado.value = (
                f"¡Felicidades, has adivinado el número en {intentos} intentos!"
            )
            resultado.color = "green"
            verificar_btn.disabled = True
        elif intento < numero_secreto:
            resultado.value = "El número es mayor"
            resultado.color = "orange"
        else:
            resultado.value = "El número es menor"
            resultado.color = "orange"
        page.update()

    def reiniciar_juego(e):
        nonlocal intentos, numero_secreto
        numero_secreto = random.randint(1, 10)
        intentos = 0
        intentos_text.value = "Intentos: 0"
        input_numero.value = ""
        resultado.value = "Adivina el Número entre 1 y 10"
        verificar_btn.disabled = False
        page.update()
        
    def cambiar_tema(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    titulo = ft.Text(
        "Cards, Dividers, Vertical Dividers en Flet",
        size=30,
        weight="bold",
        color="white",
    )

    divider_simple = ft.Divider(height=5, color=ft.Colors.BLUE_GREY_200)

    numero_secreto = random.randint(1, 10)
    intentos = 0

    input_numero = ft.TextField(label="Tu Intento", width=100)
    cambiar_tema_btn = ft.ElevatedButton(text="Cambiar Tema", on_click=cambiar_tema, bgcolor="blue")    
    verificar_btn = ft.ElevatedButton(
        text="Verificar", on_click=verificar_intentos, bgcolor="blue"
    )
    resultado = ft.Text("Adivina el Número entre 1 y 10")
    intentos_text = ft.Text("Intentos: 0")
    boton_reiniciar = ft.ElevatedButton(
        text="Reiniciar", on_click=reiniciar_juego, bgcolor="blue"
    )

    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    input_numero,
                    verificar_btn,
                    resultado,
                    intentos_text,
                    boton_reiniciar,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=10,
            border_radius=10,
        ),
        width=300,
        height=400,
    )

    card2 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Cambiar Tema",weight="bold"),
                    cambiar_tema_btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,),
            padding=10,
            border_radius=10,
        ),
        width=200,
        height=150,
    )

    divider_vertical = ft.VerticalDivider(width=5, color=ft.Colors.BLUE_GREY_200)
    divider_final=ft.Divider(height=5, color=ft.Colors.BLUE_GREY_200)

    layout = ft.Row(
        controls=[card1, divider_vertical, card2], alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(titulo, divider_simple, layout,divider_final)


ft.app(main)
