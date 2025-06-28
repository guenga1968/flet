import flet as ft


def main(page: ft.Page):
   text = ft.Text(value="Hello World", size=30, color="white")
   tex2 = ft.Text("How are you?", size=30, color="blue")
   text3 = ft.Text("This is a Flet app", size=30, color="green")
   fila = ft.Row(
       controls=[text, tex2, text3],
       alignment=ft.MainAxisAlignment.CENTER,
       spacing=50,
      
   )
   page.add(fila)
   
   boton = ft.ElevatedButton(text="Click Me")
   boton2 = ft.ElevatedButton(text="Click Me Too")
   boton3 = ft.ElevatedButton(text="Click Me Three")
   
   fila2 = ft.Row(
       controls=[boton, boton2, boton3],
       alignment=ft.MainAxisAlignment.CENTER,
       spacing=50,
   )
   page.add(fila2)
   
   columna = ft.Column(controls=[
       ft.Row(controls=[text, boton],alignment=ft.MainAxisAlignment.CENTER, expand=True, width=300),
       ft.Row(controls=[tex2, boton2]),
       ft.Row(controls=[text3, boton3]),
    ], alignment=ft.MainAxisAlignment.CENTER.CENTER, spacing=50, )
   page.add(columna)
   
    
ft.app(main)
