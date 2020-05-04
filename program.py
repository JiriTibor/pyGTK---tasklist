import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class window(Gtk.Window):
    def __init__(self):
        tasks = []

        #Initializes window
        Gtk.Window.__init__(self, title="Task list")

        grid = Gtk.Grid()
        self.add(grid)

        #Creates entry
        self.entry = Gtk.Entry()
        self.entry.set_text("")

        #Creates button for adding text
        self.button_add = Gtk.Button.new_with_label("Add")
        self.button_add.connect("clicked",self.click_add)

        # Creates button for deleting text
        self.button_delete = Gtk.Button.new_with_label("Delete")
        self.button_delete.connect("clicked", self.click_delete)

        #Appends tasks into a cell
        self.liststore = Gtk.ListStore(str)
        for x in range(0, len(tasks)):
            self.liststore.append([tasks[x]])

        treeview = Gtk.TreeView(model=self.liststore)

        #Renderes cells from list
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)
        grid.attach(treeview, 0, 2, 1, 1)

        #Renders buttons in a grid
        grid.add(self.button_add)
        grid.attach(self.button_delete, 1, 0, 2, 1)
        grid.attach(self.entry, 0, 1, 2, 1)

    def update(self):
        self.liststore.clear()
        for x in range(0, len(tasks)):
            self.liststore.append([tasks[x]])

    #Function for adding text
    def click_add(self, button):
        tasks.append(self.entry.get_text())
        print(tasks)
        self.update()

    #Function for deleting text
    def click_delete(self, button):
        tasks.remove(self.entry.get_text())
        self.update()

win = window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
tasks = []
Gtk.main()