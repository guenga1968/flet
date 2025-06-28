import flet as ft

def main(page: ft.Page):
    page.title = "Tareas"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text("Lista de Tareas",size=30,color="white",weight="bold",)
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea= ft.ListTile(
                title=ft.Text(campo_tarea.value),
                leading=ft.Checkbox(on_change=seleccionar_tarea),
            )
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()
            
    def seleccionar_tarea(e):
        seleccionadas =[t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = f"Tareas Seleccionadas: " + ", ".join(seleccionadas)
        page.update()
    
    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()
        
        
    campo_tarea = ft.TextField(hint_text="Escribe una Nueva Tarea",)
    
    boton_agregar = ft.ElevatedButton("Agregar Tarea",  on_click=agregar_tarea, 
                                      style= ft.ButtonStyle(
                                          bgcolor=ft.Colors.RED_900,
                                          padding=20,
                                          color=ft.Colors.WHITE
                                      ))
    tareas =[]
    tareas_seleccionadas = ft.Text("", size=20, weight="bold", color="white")
    
    lista_tareas = ft.ListView(expand=1,spacing=3)
    
    page.add(titulo,campo_tarea,boton_agregar,lista_tareas, tareas_seleccionadas)
ft.app(main)