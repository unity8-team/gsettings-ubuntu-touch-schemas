pkladir = $(localstatedir)/lib/polkit-1/localauthority/10-vendor.d
dist_pkla_DATA = 50-com.ubuntu.AccountsService.pkla

policydir = $(datadir)/polkit-1/actions
dist_policy_DATA = com.ubuntu.AccountsService.policy

accountsservice_schemas = \
	com.ubuntu.AccountsService.Sound.xml \
	com.ubuntu.touch.AccountsService.SecurityPrivacy.xml \
	com.ubuntu.touch.AccountsService.Sound.xml

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

