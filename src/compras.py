import flet as ft


def main(page: ft.Page):
    page.title = "Lista de Compras"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.padding = 20

    titulo = ft.Text(
        "Lista de Compras en Flet",
        size=30,
        color="white",
        text_align="center",
        weight="bold",
    )

    shopping_list = ft.Column(scroll=ft.ScrollMode.AUTO)

    item_input = ft.TextField(
        hint_text="Añadir articulo ...",
        border_color="amber",
        color="white",
        text_align="center",
        width=300,
    )
    quantity_input = ft.TextField(
        hint_text="Cantidad",
        border_color="amber",
        color="white",
        text_align="center",
        width=100,
    )
    categories = ["Sin Categoría", "Alimentos", "Limpieza", "Electrónica", "Ropa"]

    def add_item(e):
        if item_input.value:
            quantity = quantity_input.value if quantity_input.value else 1

            def update_category(e):
                category_text.value = f"Categoria: {e.control.value}"
                page.update()

            category_dropdown = ft.Dropdown(
                options=[ft.dropdown.Option(category) for category in categories],
                value=categories[0],
                on_change=update_category,
                color="amber",
                width=150,
            )
            category_text = ft.Text(
                f"Categoria: {categories[0]}", color=ft.Colors.AMBER_200
            )
            new_item= ft.ListTile(
                leading=ft.Checkbox(value=False,fill_color="amber"),
                title=ft.Text(f"{item_input.value} X ({quantity})", color="white"),
                subtitle=ft.Row(
                    controls=[category_text, category_dropdown],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    ),
                trailing=ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="red",
                    on_click=lambda _: shopping_list.controls.remove(new_item) or page.update(),
                )
            )
            shopping_list.controls.append(new_item)
            item_input.value = ""
            quantity_input.value = ""
            page.update()
            
    add_button=ft.OutlinedButton("Añadir a la Lista", on_click=add_item,
                                 style=ft.ButtonStyle(
                                     padding=ft.padding.all(20),
                                     color=ft.Colors.AMBER, 
                                     side=ft.border.BorderSide(2, color=ft.Colors.AMBER)
                                 ))
    
    fila_input = ft.Row(
        controls=[item_input, quantity_input, add_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    
    def clear_list(e):
        shopping_list.controls.clear()
        page.update()
        
    clear_button = ft.IconButton(
        icon=ft.Icons.CLEANING_SERVICES,
        tooltip="Limpiar Lista",
        icon_color="amber",
        on_click=clear_list,
    )
    
    def show_stats(e):
        total_items = len(shopping_list.controls)
        checked_items = sum([1 for item in shopping_list.controls if item.leading.value])
        category_counts = {}
        for item in shopping_list.controls:
            category = item.subtitle.controls[1].value
            category_counts[category] = category_counts.get(category, 0) + 1
            stats_text= f"Total de Articulos: {total_items} Comprados: {checked_items} Categorias: {category_counts}\n"
            stats_text += "Categorias\n" + "\n".join([f"{category}: {count}" for category, count in category_counts.items()])
            
        snackbar = ft.SnackBar(ft.Text(stats_text, color="black"), bgcolor="amber")
        page.overlay.append(snackbar)
        snackbar.open = True
        page.update()
    
    stats_button = ft.TextButton(
        
        text="Estadisticas",
        style= ft.ButtonStyle(
            color=ft.Colors.AMBER,),
        on_click=show_stats,
    )
        
    
    fila_botones = ft.Row(
        controls=[clear_button, stats_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    page.add(titulo, fila_input,fila_botones, shopping_list)


ft.app(main)
