import flet as ft 

def main(page:ft.Page):
    page.title="Uso de ref"
    
    miBoton=ft.Ref[ft.ElevatedButton]()
    mi_Barra=ft.Ref[ft.AppBar]()
    
    ft.AppBar(ref=mi_Barra, title=ft.Text("Mi Barra"), center_title=True, bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST)
    
    def mostrar_texto(e):
       miBoton.current.text="Boton Presionado"
       mi_Barra.current.title=ft.Text("Boton Presionado")
       miBoton.current.update()
       mi_Barra.current.update()
    
    ft.ElevatedButton(text="Presioname", on_click=mostrar_texto, ref=miBoton)
   

    page.add(mi_Barra.current,miBoton.current)

ft.app(target=main)