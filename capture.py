#import glib
#import dbus
#from dbus.mainloop.glib import DBusGMainLoop

#def notifications(bus, message):
#    if message.get_member() == "Notify":
#        print [arg for arg in message.get_args_list()]

#DBusGMainLoop(set_as_default=True)

#bus = dbus.SessionBus()
#bus.add_match_string_non_blocking("interface='org.freedesktop.Notifications'")
#bus.add_message_filter(notifications)

#mainloop = glib.MainLoop()
#mainloop.run()

import dbus, gobject, subprocess, glib
from dbus.mainloop.glib import DBusGMainLoop

def send_notifier(dbus, message):
    if message.get_member() == "Notify":
        subprocess.check_call(['/home/maschmann/git/libnotifyCapture/test'])

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("interface='org.freedesktop.Notifications'")
bus.add_message_filter(send_notifier)

mainloop = glib.MainLoop()
mainloop.run()