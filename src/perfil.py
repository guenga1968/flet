import flet as ft

def main(page: ft.Page):
    page.title = "Configurador de Perfil de Usuario"
    page.padding = 20
    page.scroll = "always"
    
    page.theme_mode = ft.ThemeMode.LIGHT
    
    titulo = ft.Text("Perfil de Usuario", size=28, weight="bold", color=ft.Colors.PINK_300)
    
    
    preview= ft.Text("Completa el Formulario para visualizar perfil", size=14)
    
    def update_preview(e):
        preview.value=f"""
        Nombre: {name_input.value}
        Edad: {age_dropdown.value}
        Genero: {gender_radio.value}
        Intereses: {', '.join([i.label for i in interest_check.controls if i.value])}
        Modo Oscuro:{"Activado" if theme_switch.value else "Desactivado"}
        """
        page.update()
    
    name_input= ft.TextField(label="Nombre",border_radius=8, on_change=update_preview)
    
    age_dropdown= ft.Dropdown(
        label="Edad",
        options=[ft.dropdown.Option(str(age)) for age in range(18,101)],
        border_radius=8,
        on_change=update_preview
    )
    gender_radio= ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro"),
       ] ), on_change=update_preview
    )
    gender_radio.on_change=update_preview
    
    interest=["Arte","Tecnología","Deportes","Música","Viajes"]
    
    interest_check= ft.Column(
        controls=[ft.Checkbox(label=interest, on_change=update_preview) for interest in interest],
        
    )   
    def toggle_theme(e):
        if theme_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
            titulo.color=ft.Colors.BLUE_300
            theme_switch.label = "Modo Claro"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            titulo.color=ft.Colors.PINK_300
            theme_switch.label = "Modo Oscuro"
        page.update()
    
    theme_switch = ft.Switch(label="Modo Oscuro", on_change=lambda e: [update_preview(e), toggle_theme(e)])
    
    page.add(titulo, name_input, age_dropdown,
             ft.Text("Genero:", size =16, weight="bold"),
             gender_radio, 
             ft.Text("Intereses:", size =16, weight="bold"),
             interest_check,
             ft.Text("Tema:", size =16, weight="bold"),
             theme_switch,
             ft.Text("Previsualización:", size =16, weight="bold"),
             preview
             )


ft.app(target=main)