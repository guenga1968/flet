import flet as ft


def main(page: ft.Page):
    page.title = "Biblioteca de Flet"
    page.theme_mode = ft.ThemeMode.DARK

    def change_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        theme_icon_button.icon = (
            ft.Icons.DARK_MODE
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.LIGHT_MODE
        )
        page.update()

    
            
    
    theme_icon_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE, tooltip="Cambiar Tema", on_click=change_theme
    )

    titulo = ft.Text("Mi Biblioteca de Personal")

    app_bar = ft.AppBar(
        title=titulo,
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[theme_icon_button],
    )
    def add_book(e):
        if not title_field.value:
            title_field.error_text = "Por favor, ingresa un título"
            page.update()
            return
        new_book = ft.ListTile(
            title=ft.Text(title_field.value),
            subtitle=ft.Text(autor_field.value) if autor_field.value else ft.Text("Autor Desconocido"),
            trailing=ft.PopupMenuButton(
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        text="Eliminar",
                        on_click=lambda _: books_view.controls.remove(new_book) or page.update(),
                    ),
                    ft.PopupMenuItem(
                        text="Agregar a la Lista de Deseados",
                        on_click=lambda _: whislist_view.controls.append(new_book) or page.update(),
                    ),
                ],
            ),
        )
        books_view.controls.append(new_book)
        title_field.value = ""
        autor_field.value = ""
        title_field.error_text = None
        page.update()
        
        
       

    books_view = ft.ListView(expand=1,spacing=10, padding=20)
    whislist_view = ft.ListView(expand=1, spacing=10, padding=20,)

    title_field = ft.TextField(label="Título del Libro", width=300)
    autor_field = ft.TextField(label="Autor", width=300)
    add_button = ft.ElevatedButton(text="Añadir Libro", on_click=add_book)

    add_book_view = ft.Column(
        [
            ft.Text("Añadir Nuevo Libro", size=20, weight=ft.FontWeight.BOLD),
            title_field,
            autor_field,
            add_button,
        ],
        spacing=20,
    )
    def destination_change(e):
        index = e.control.selected_index
        content.controls.clear()
        if index == 0:
            content.controls.append(books_view)
        elif index == 1:
            content.controls.append(add_book_view)
        elif index == 2:
            content.controls.append(whislist_view)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.BOOK, label="Mis Libros"),
            ft.NavigationRailDestination(icon=ft.Icons.ADD, label="Añadir Libro"),
            ft.NavigationRailDestination(icon=ft.Icons.FAVORITE, label="Lista de Deseos" ),
        ],
        on_change=destination_change,
    )

    content = ft.Column(controls=[books_view],expand=True,)

    page.add(app_bar, ft.Row([rail,ft.VerticalDivider(), content], expand=True))


ft.app(target=main)
