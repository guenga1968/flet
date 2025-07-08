import flet as ft


def main(page: ft.Page):
    page.title = "Tareas Pendientes",
    page.icon = "assets/icono.png"
    page.padding = 0

    def agregar_tarea(e):
        if input_text.value:
            tarea = ft.Checkbox(
                label=input_text.value, value=False, on_change=chek_tarea
            )
            lista.controls.append(tarea)
            input_text.value = ""
            input_text.focus()
            page.update()

    def chek_tarea(e):
        if e.control.value:
            tarea = e.control.label
            lista.controls.remove(e.control)
            page.update()

    input_text = ft.TextField(
        hint_text="Escribe una Nueva Tarea", on_submit=agregar_tarea
    )
    boton = ft.ElevatedButton(text="Agregar", on_click=agregar_tarea)

    fila = ft.Row(controls=[input_text, boton], alignment=ft.MainAxisAlignment.CENTER)

    lista = ft.ListView(expand=True)

    contenedor = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[ft.Text("Tareas Pendientes"), fila, lista], alignment=ft.MainAxisAlignment.CENTER,
        
        ),
        padding=20,
        bgcolor=ft.Colors.BLUE_GREY_800,
    )

    page.add(contenedor)


ft.app(target=main)
