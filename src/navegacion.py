import flet as ft

def main(page: ft.Page):
    page.title = "Navegación en Flet"
    page.padding = 20
    
    titulo =ft.Text("Ejemplo de Navegación en Flet", size=24, color="white")
    
    def on_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go("/home")
        elif selected_index == 1:
            page.go("/search")
        elif selected_index == 2:
            page.go("/configuration")
        page.update()
    
    navigation_bar= ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuration"),
        ],
        on_change=on_navigation_change,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        indicator_color=ft.Colors.PRIMARY_CONTAINER,
        )
    
    page.add(titulo, navigation_bar)


ft.app(target=main)