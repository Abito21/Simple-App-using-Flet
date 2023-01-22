# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indrswara
"""

import flet as ft

class tasksApp(ft.UserControl):

    def build(self):
        self.textField = ft.TextField(width=350)
        self.addBtn = ft.FloatingActionButton(icon= ft.Icon.ADD,
                                              on_click=self.addClick)
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[
            ft.Row(controls=[self.textField, self.addBtn]),
            self.tasks
        ])

    def addClick(self, e):
        pass

    def taskDelete(self, task):
        pass

def main(page: ft.Page):
    page.title = "Tasking App by AbidIndraswara"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "WHITE"

    taskingApp = tasksApp
    page.add(taskingApp)

ft.app(target=main)