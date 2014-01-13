accountsservice_schemas = \
	com.ubuntu.touch.AccountsService.SecurityPrivacy.xml

EXTRA_DIST =				\
	$(accountsservice_schemas)	

install-data-hook:
	$(MKDIR_P) $(DESTDIR)$(datadir)/dbus-1/interfaces			\
		       $(DESTDIR)$(datadir)/accountsservice/interfaces
	
	for file in $(accountsservice_schemas); do 							\
		$(INSTALL_DATA) $$file $(DESTDIR)$(datadir)/dbus-1/interfaces;	\
		$(LN_S) ../../dbus-1/interfaces/$$file							\
             	$(DESTDIR)$(datadir)/accountsservice/interfaces;		\
	done

CLEANFILES =						\
	$(accountsservice_schemas)

