import flet as ft
import time

def main(page:ft.Page):
    page.title = "Simulador de Descarga"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    titulo = ft.Text("Simulador de Descarga de Archivos", size=30, color=ft.Colors.BLUE_GREY_100, weight="bold",)
    archivos= ft.Text("Selecciona los Archivos a Descargar", size=15, color="white",)
    file_list= ft.Column([
        ft.Checkbox("Documento PDF (2.5 MB)",value=False),
        ft.Checkbox("Imagen JPG (5 MB)",value=False),
        ft.Checkbox("Video MP4 (50 MB)",value=False),
        ft.Checkbox("Archivo ZIP (100 MB)",value=False),
    ])
    
    def simular_descarga(e):
        archivos_seleccionados= [checkbox for checkbox in file_list.controls if checkbox.value]
        if not archivos_seleccionados:
            status_text.value = "Por favor, selecciona al menos un archivo."
            page.update()
            return
        progres_bar.value = 0
        progres_ring.value = 0
        page.update()
        
        total_size= sum([float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in archivos_seleccionados])
        downloaded=0
        for archivo in archivos_seleccionados:
            size= float(archivo.label.split("(")[1].split(" MB")[0])
            status_text.value = f"Descargando {archivo.label}"
           
            for _ in range(10):
               time.sleep(0.3)
               downloaded += size/10
               progress=min(downloaded/total_size,1)
               progres_bar.value = progress
               progres_ring.value = progress
               page.update()
        progres_bar.value = 1
        progres_ring.value = 1
        status_text.value = "Descarga Completa"
        page.update()
        time.sleep(1)
        progres_bar.value = 0
        progres_ring.value = 0
        status_text.value = ""
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()
    
    contenedor= ft.Container(content=file_list, padding=20)
    
    progres_bar= ft.ProgressBar(width=400,color="amber", bgcolor="#263238", value=0)
    progres_ring= ft.ProgressRing(stroke_width=5,color="amber", value=0)
    status_text=ft.Text("", color="white")
    fila= ft.Row(controls=[progres_bar,progres_ring], alignment=ft.MainAxisAlignment.CENTER)
    boton_descarga= ft.ElevatedButton("Iniciar Descarga",on_click=simular_descarga, bgcolor="amber",color="black")
    
   
    page.add(titulo, archivos, contenedor, fila,status_text, boton_descarga)


ft.app(target=main)