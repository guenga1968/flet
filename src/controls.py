import flet as ft


def main(page):

    page.title="Pruebas de Flet"
    
    def agregar_tarea(e):
        page.add(ft.Text(txt_file.value))
        txt_file.value = ""
        page.update()
    
    txt_file=ft.TextField(label="Ingresa Tarea")

    btn_agregar=ft.ElevatedButton(text="Agregar", on_click=agregar_tarea)

    page.add(txt_file, btn_agregar)
ft.app(main)