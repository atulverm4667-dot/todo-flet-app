import flet as ft

def main(page: ft.Page):
    page.title = "Mera Pehla App"
    page.theme_mode = ft.ThemeMode.DARK 
    
    # PC par run karte waqt mobile jaisa size dikhane ke liye
    page.window_width = 400
    page.window_height = 650

    task_input = ft.TextField(hint_text="Aaj kya karna hai?", width=250)
    tasks_list = ft.Column()

    def add_task(e):
        if task_input.value != "": 
            tasks_list.controls.append(ft.Checkbox(label=task_input.value))
            task_input.value = "" 
            page.update() 

    add_btn = ft.ElevatedButton("Add", on_click=add_task, color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_800)

    page.add(
        ft.Text("To-Do List", size=30, weight="bold", color=ft.colors.BLUE_400),
        ft.Row([task_input, add_btn]),
        tasks_list
    )

# NORMAL NATIVE MODE (Bina Server ke)
ft.app(target=main)