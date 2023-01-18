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
    entriesRow = ft.Row(controls=[textField, addBtn], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(entriesRow)


ft.app(target=main)