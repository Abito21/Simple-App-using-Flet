# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indraswara
"""

import flet as ft

def main(page: ft.Page):

    def addTask(p):
        checkBox = ft.Checkbox(value=False)
        checkBoxText = ft.Text(value=textField.value, width=350, bgcolor="#00337C", size=15, color="WHITE")
        taskRow = ft.Row(controls=[checkBox, checkBoxText],
                         alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)

    page.window_width = 500
    page.window_height = 900
    page.bgcolor = "#00337C"

    # Text Box
    textField = ft.TextField(width=350)
    addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addTask)

    # Check Box
    checkBox = ft.Checkbox(value=True)
    checkBoxText = ft.Text(value="Task 1", width=350, bgcolor="#00337C", size=15, color="WHITE")

    entriesRow = ft.Row(controls=[textField, addBtn], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


    page.add(entriesRow)


ft.app(target=main)