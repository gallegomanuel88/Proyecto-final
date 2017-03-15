# -*- coding: utf-8 -*-
import sys
#import Adafruit_DHT
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

"""humidity, temperature = Adafruit_DHT.read_retry(22, 4)

temperaturaString = '{0:0.1f}C'.format(temperature)
humedadString = '{0:0.1f}%'.format(humidity)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    print(temperaturaString, humedadString)
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)"""

class Ventana(Gtk.Window):

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_button1_clicked(self, button):
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        temperaturaString = '{0:0.1f}C'.format(temperature)
        humedadString = '{0:0.1f}%'.format(humidity)
        self.comboLista.insert(0, "0", textoRecogido)

    def on1_button2_clicked(self, button):
        #self.comboLista.remove()
        print("holi")

    def __init__(self):
        Gtk.Window.__init__(self, title="Parametros invernadero")
        self.set_border_width(10)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)


        self.builder = Gtk.Builder()
        self.builder.add_from_file("Interfaz.glade")

        senal1 = {"on_button1_clicked": self.on_button1_clicked}
        self.builder.connect_signals(senal1)
        senal2 = {"on_button1_clicked": self.on1_button2_clicked}
        self.builder.connect_signals(senal2)

        self.boxGlade = self.builder.get_object("box1")
        self.box.add(self.boxGlade)
        self.box.pack_start(self.boxGlade, False, False, 0)


window = Ventana()
window.show_all()
Gtk.main()
