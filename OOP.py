# -*- coding: utf-8 -*-
"""

@author: Abid Juliant Indrswara
"""

import flet as ft

class tasksApp(ft.UserControl):

    def build(self):
        self.textField = ft.TextField(width=350)
        self.addBtn = ft.FloatingActionButton(icon= ft.icons.ADD,
                                              on_click=self.addClick)
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[
            ft.Row(controls=[self.textField, self.addBtn]),
            self.tasks
        ])
        return taskRow

    def addClick(self, e):
        task = Task(self.textField.value, self.taskDelete)
        self.tasks.controls.append(task)
        self.textField.value = ""
        self.update()

    def taskDelete(self, task):
        pass

class Task(ft.UserControl):
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete
    
    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False)
        self.editName = ft.TextField()

        self.displayView = ft.Row(controls=[self.displayTask,
                                  ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED,
                                                                 on_click=self.editClick),
                                                   ft.IconButton(ft.icons.DELETE_OUTLINED,
                                                                 on_click=self.deleteClick)])])
        self.editView = ft.Row(visible=False,
                               controls=[self.editName,
                                         ft.IconButton(ft.icons.DELETE_OUTLINED,
                                                       on_click=self.saveClick)])
        return ft.Column(controls=[self.displayView, self.editView])

    def editClick(self, e):
        pass
    
    def saveClick(self, e):
        pass
    
    def deleteClick(self, e):
        pass

def main(page: ft.Page):
    page.title = "Tasking App by AbidIndraswara"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "WHITE"

    taskingApp = tasksApp()
    page.add(taskingApp)

ft.app(target=main)