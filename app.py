# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indraswara
"""

import flet as ft

def main(page: ft.Page):

    page.window_width = 500
    page.window_height = 900
    textField = ft.TextField()
    addBtn = ft.ElevatedButton(text="Add")

    page.add(textField,
             addBtn)


ft.app(target=main)