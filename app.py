# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indraswara
"""

import flet as ft

def main(page: ft.Page):

    page.window_width = 500
    page.window_height = 900
    page.bgcolor = "#00337C"
    textField = ft.TextField(width=350)
    addBtn = ft.ElevatedButton(text="Add")

    checkBox = ft.Checkbox(value=True)
    checkBoxText = ft.Text(value="Task 1", width=350, bgcolor="WHITE", size=24)

    taskRow = ft.Row(controls=[checkBox, checkBoxText],
                     alignment=ft.MainAxisAlignment.START)
    entriesRow = ft.Row(controls=[textField, addBtn], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


    page.add(entriesRow, taskRow)


ft.app(target=main)