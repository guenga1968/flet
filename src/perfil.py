import flet as ft

def main(page: ft.Page):
    page.title = "Perfil de Usuario"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.add(ft.Text("Perfil"))


ft.app(target=main)