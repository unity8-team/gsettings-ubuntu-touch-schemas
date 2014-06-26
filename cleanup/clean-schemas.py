#!/usr/bin/python3

from gi.repository import Gio
from gi.repository import Click

clickdb = Click.DB.new()
clickdb.read()

pkgnames = [] 
for package in clickdb.get_packages(False) :
	pkgnames.append(package.get_property('package'))

settings = Gio.Settings.new('com.ubuntu.touch.notifications')
goodapps = []

for appname in settings.get_value('popup-blacklist').unpack() :
	if not appname[0] in pkgnames and appname[0] == appname[1] :
		appinfo = Gio.DesktopAppInfo.new(appname[0] + ".desktop")
		if not appinfo is None :
			goodapps.append(appname)
	else :
		goodapps.append(appname)

settings.set_strv('popup-blacklist', goodapps)
