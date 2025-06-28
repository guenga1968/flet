import flet as ft
import os
import base64

def main(page: ft.Page):
    page.title ="Galería de Productos"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    
    
    def crear_producto(nombre, precio, color, imagen_nombre):
        imagen_path = os.path.join(os.path.dirname(__file__), "assets", imagen_nombre)
        try:
            with open(imagen_path, "rb") as imagen_file:
                imagen_bytes = base64.b64encode(imagen_file.read()).decode()
        except FileNotFoundError:
            print(f"La Imagen {imagen_nombre}no fue encontrada en: {imagen_path}")
            imagen_bytes = None
              
        return ft.Container(
        content= ft.Column([
            ft.Image(src_base64=imagen_bytes, 
                     width=150,
                     height=150,
                     fit=ft.ImageFit.CONTAIN,
                     error_content=ft.Text("Imagen no disponible"),) if imagen_bytes else ft.Text("Imagen no disponible"),
            ft.Text(nombre, size=16,  weight="bold",),
            ft.Text(f"${precio}", size=14),
            ft.ElevatedButton("Agregar al Carrito", color=ft.Colors.WHITE),
            ]),
        bgcolor=color,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center,
    )
        
    productos =[
                crear_producto("Producto 1", "19.99", ft.Colors.BLUE_500, "flor.jpeg"),
                crear_producto("Producto 2", "29.99", ft.Colors.PINK_500,"hotel.jpeg"),
                crear_producto("Producto 3", "39.99", ft.Colors.PURPLE_500, "montaña.jpeg"),
                crear_producto("Producto 4", "49.99", ft.Colors.CYAN_500, "pajaro.jpeg"),
                crear_producto("Producto 5", "59.99", ft.Colors.GREEN_500, "parque.jpeg"),
                ]
       
    galeria =ft.ResponsiveRow(
        [ft.Container(producto, col={"sm":12,"md":6, "lg":3}) for producto in productos],
        run_spacing=20,
        spacing=20,
    )
    
    
    contenido = ft.Column([
        ft.Text("Galería de Productos", size=32, color="white", weight="bold",),
        ft.Divider(height=20,color=ft.Colors.WHITE24),
        galeria
        
    ], scroll=ft.ScrollMode.AUTO,expand=True) 
    
    page.add(contenido)
    

ft.app(main)