import flet as ft
from openpyxl import Workbook
from datetime import datetime



def main(page: ft.Page):
    page.title = "Data Table en Flet con Excel"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo= ft.Text("DataTable en Flet", size=24, color="white")
    
    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_700,
        border= ft.border.all(width=2, color=ft.Colors.BLUE_GREY_100),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(width=2, color=ft.Colors.BLUE_GREY_100),
        horizontal_lines=ft.border.BorderSide(width=2, color=ft.Colors.BLUE_GREY_100),
        columns=[
            ft.DataColumn(ft.Text("ID", color= ft.Colors.BLUE_200)),
            ft.DataColumn(ft.Text("Nombre", color= ft.Colors.BLUE_200)),
            ft.DataColumn(ft.Text("Edad", color= ft.Colors.BLUE_200)),
            ],
        rows=[],
    )
    
    def agregar_fila(e):
        nueva_fila = ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(len(data_table.rows) + 1), color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(input_nombre.value, color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(input_edad.value, color=ft.Colors.WHITE)),
        ])
        data_table.rows.append(nueva_fila)
        input_nombre.value = ""
        input_edad.value = ""
        page.update()
    
    def guardar_excel(e):
        wb= Workbook()
        ws = wb.active
        ws.title = "Data Table en Flet"
        ws.append(["ID", "Nombre", "Edad"])
        for row in data_table.rows:
            ws.append([row.cells[0].content.value, row.cells[1].content.value, row.cells[2].content.value])
       
        fecha_actual = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
        nombre_archivo= f"{fecha_actual}_datosTabla.xlsx"
        wb.save(nombre_archivo)
        snack_bar = ft.SnackBar(ft.Text(f"Archivo Guardado en {nombre_archivo}"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
    
    
    input_nombre = ft.TextField(hint_text="Escribe tu Nombre",bgcolor=ft.Colors.BLUE_GREY_700, color=ft.Colors.WHITE)
    input_edad = ft.TextField(hint_text="Escribe tu Edad",bgcolor=ft.Colors.BLUE_GREY_700, color=ft.Colors.WHITE)
    boton_agregar = ft.ElevatedButton(text="Agregar Fila", on_click=agregar_fila, bgcolor="green", color="white",
                                      style= ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                            padding=ft.Padding(top=5, bottom=10, left=10, right=10))) 
    boton_guardar= ft.ElevatedButton(text="Guardar en Excel", on_click=guardar_excel,bgcolor="blue",color="white", 
                                     style= ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                           padding=ft.Padding(top=5, bottom=10, left=10, right=10))) 
    
    input_container= ft.Row([input_nombre, input_edad, boton_agregar, boton_guardar], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(titulo, data_table, input_container)
    
    

ft.app(main)
    