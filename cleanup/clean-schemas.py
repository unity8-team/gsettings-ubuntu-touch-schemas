#!/usr/bin/python3

from gi.repository import GLib
from gi.repository import Gio
from gi.repository import Click

def tup2variant (tup) :
	builder = GLib.VariantBuilder.new(GLib.VariantType.new("(ss)"))
	builder.add_value(GLib.Variant.new_string(tup[0]))
	builder.add_value(GLib.Variant.new_string(tup[1]))
	return builder.end()

clickdb = Click.DB.new()
clickdb.read()

pkgnames = [] 
for package in clickdb.get_packages(False) :
	pkgnames.append(package.get_property('package'))

settings = Gio.Settings.new('com.ubuntu.touch.notifications')
goodapps = GLib.VariantBuilder.new(GLib.VariantType.new("a(ss)"))

for appname in settings.get_value('popup-blacklist').unpack() :
	if appname[0] in pkgnames :
		goodapps.add_value(tup2variant(appname))
	elif (appname[0] == appname[1]) :
		appinfo = Gio.DesktopAppInfo.new(appname[0] + ".desktop")
		if not appinfo is None :
			goodapps.add_value(tup2variant(appname))

settings.set_value('popup-blacklist', goodapps.end())
