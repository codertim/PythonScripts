import gi
import time

gi.require_version("Gtk", "3.0")
gi.require_version("Notify", "0.7")

from gi.repository import Gtk
from gi.repository import Notify

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Message Notifier")
        Gtk.Window.set_default_size(self, 640, 480)
        Notify.init("simple GTK3 Application")

        self.box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.button = Gtk.Button(label="Go")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.END)   # CENTER
        self.button.connect("clicked", self.handle_btn_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.lbl = Gtk.Label(angle=1)
        self.lbl.set_label("Enter seconds:")
        # self.lbl.set_halign(Gtk.Align.CENTER)
        self.box.add(self.lbl)

        hboxForEntry = Gtk.Box(spacing=6)
        self.entry = Gtk.Entry()
        # self.entry.set_width_chars(8)
        # self.entry.set_size_request(30, 30)
        self.entry.set_text("5")
        print("self entry props: ", dir(self.entry.props))
        #self.box.pack_start(self.entry, True, True, 0)
        # hboxForEntry.pack_start(self.entry, True, True, 0)
        hboxForEntry.add(self.entry)
        hboxForEntry.set_halign(Gtk.Align.CENTER)
        self.entry.set_valign(Gtk.Align.START)
        self.box.pack_start(hboxForEntry, True, True, 0)

        hbox = Gtk.Box(spacing=2)
        self.box.pack_start(hbox, True, True, 0)

        # spinner
        self.spinner = Gtk.Spinner()
        self.box.add(self.spinner)
        # self.box.pack_start(hbox, True, True, 0)


    def handle_btn_clicked(self, widget):
        # sec = int(self.entry.get_text())
        props = self.entry.get_properties('text')
        print('props text:', props)
        print('props text:type', type(props))
        sec = int(props[0])
        print("seconds: ", sec)
        self.spinner.start()
        time.sleep(sec)
        self.spinner.stop()
        n = Notify.Notification.new("Notifier", "Hello")
        n.show()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



