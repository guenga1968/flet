import flet as ft
import random

def main(page: ft.Page):
    page.title = "Tabs en Flet"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def generar_tareas():
        tareas=[
            "Hacer las Compras", "Buscar Matafuegos", "Visitar a Papá", "Preparar todo para el viaje", "Lavar la ropa","pasear al perro",
        ]
        return random.sample(tareas, 4)
    

    tareas =generar_tareas()
    lista_tareas = ft.ListView(
        controls=[ft.Text(tarea, color="white") for tarea in tareas],
        spacing=10,
        padding=20,
    )
    def actualizar_tareas(e):     
        lista_tareas.controls.clear()
        tareas = generar_tareas()
        for tarea in tareas:
            lista_tareas.controls.append(ft.Text(tarea, color="white"))
        page.update()
    
    titulo = ft.Text("Ejemplo de Tabs en Flet", size=24, color="white")
    actualizar_btn= ft.ElevatedButton(text="Actualizar", on_click=actualizar_tareas)
    
    contenido_tareas = ft.Column(
        controls=[
            lista_tareas,
        actualizar_btn
        ],
       
        )
    
    campo_nombre= ft.TextField(label="Nombre", hint_text="Escribe tu Nombre", color="white", bgcolor=ft.Colors.BLUE_GREY_700,)
    campo_apellido= ft.TextField(label="Apellido", hint_text="Escribe tu Apellido", color="white", bgcolor=ft.Colors.BLUE_GREY_700,)
    boton_guardar= ft.ElevatedButton("Guardar Perfil")
    contenido_perfil = ft.Container(
        padding=20,
        content= ft.Column(
        controls=[
            campo_nombre,
            campo_apellido,
            boton_guardar
        ],
       
    ))
    
    switch_notificaciones= ft.Switch(label="Notificaciones", value=False)
    slider_volumen= ft.Slider(min=0, max=100, divisions=10, label="Volumen") 
    contenido_configuracion=ft.Container(
        padding=20,
        content= ft.Column(
            controls=[
                switch_notificaciones,
                slider_volumen
            ]
        )
    )
    
    tabs= ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
        ft.Tab(text="Tareas", icon=ft.Icons.LIST_ALT, content=contenido_tareas),
        ft.Tab(text="Perfil", icon=ft.Icons.PERSON, content=contenido_perfil),
        ft.Tab(text="Configuración", icon=ft.Icons.SETTINGS,content=contenido_configuracion),
    ],
        expand=1,
        )
   
    page.add(titulo, tabs)


ft.app(main)