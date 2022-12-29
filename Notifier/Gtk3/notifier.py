import gi
import time

gi.require_version("Gtk", "3.0")
gi.require_version("Notify", "0.7")

from gi.repository import Gtk
from gi.repository import Notify

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello")
        Gtk.Window.set_default_size(self, 640, 480)
        Notify.init("simple GTK3 Application")

        self.box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.button = Gtk.Button(label="click here!")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)
        self.button.connect("clicked", self.handle_btn_clicked)
        self.box.pack_start(self.button, True, True, 0)

        hboxForEntry = Gtk.Box(spacing=6)
        self.entry = Gtk.Entry()
        # self.entry.set_width_chars(8)
        # self.entry.set_size_request(30, 30)
        self.entry.set_text("seconds")
        #self.box.pack_start(self.entry, True, True, 0)
        hboxForEntry.pack_start(self.entry, True, True, 0)
        self.box.pack_start(hboxForEntry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        self.box.pack_start(hbox, True, True, 0)


    def handle_btn_clicked(self, widget):
        sec = int(self.entry.get_text())
        print("seconds: ", sec)
        time.sleep(sec)
        n = Notify.Notification.new("My GTK3 Application", "Hello")
        n.show()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



