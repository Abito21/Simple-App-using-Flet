# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indrswara
"""

import flet as ft

def main(page: ft.Page):
    page.title = "Tasking App by AbidIndraswara"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "WHITE"

ft.app(target=main)