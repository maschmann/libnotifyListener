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

#!/usr/bin/env python
import dbus, gobject, subprocess
from dbus.mainloop.glib import DBusGMainLoop

def send_notifier():
    subprocess.check_call(['sudo /usr/bin/ledcontroller', 'red'])
    subprocess.check_call(['sudo /usr/bin/ledcontroller', 'yellow'])
    subprocess.check_call(['sudo /usr/bin/ledcontroller', 'off'])

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_signal_receiver(send_notifier, dbus_interface="org.freedesktop.Notifications")
#bus.add_message_filter(notifications)

loop = gobject.MainLoop()
loop.run()