accountsservice_schemas = \
	com.ubuntu.touch.AccountsService.SecurityPrivacy.xml

EXTRA_DIST =				\
	$(accountsservice_schemas)	

install-exec-hook:
	$(MKDIR_P) $(DESTDIR)/usr/share/dbus-1/interfaces			\
		       $(DESTDIR)/usr/share/accountsservice/interfaces
	
	for file in $(accountsservice_schemas); do 					\
		$(LN_S) ../../dbus-1/interfaces/$$file					\
             	$(DESTDIR)/usr/share/accountsservice/interfaces;\
	done

CLEANFILES =						\
	$(gsettings_SCHEMAS)			\
	$(desktop_gschemas_in)			\
	*.gschema.valid

