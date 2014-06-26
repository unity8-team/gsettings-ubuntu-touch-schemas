
CLICK_HOOK_OUTPUT=$(top_srcdir)/debian/gsettings-ubuntu-schemas.touch-schemas-clean.click-hook 

all: $(CLICK_HOOK_OUTPUT)

$(CLICK_HOOK_OUTPUT): touch-schemas-clean.click-hook.in Makefile
	$(AM_V_GEN) $(SED) -e 's^\@pkgdatadir\@^$(pkgdatadir)^g' < $< > $@

%.conf: %.conf.in Makefile
	$(AM_V_GEN) $(SED) -e 's^\@pkgdatadir\@^$(pkgdatadir)^g' < $< > $@

upstart_jobs_in = \
	touch-schemas-clean.conf.in

upstart_jobs_DATA = $(upstart_jobs_in:.conf.in=.conf)
upstart_jobsdir = $(datadir)/upstart/sessions

upstart_scripts_SCRIPTS = \
	clean-schemas.py
upstart_scriptsdir = $(pkgdatadir)

EXTRA_DIST = \
	touch-schemas-clean.click-hook.in \
	$(upstart_jobs_in) \
	$(upstart_scripts_SCRIPTS)

CLEANFILES = \
	$(CLICK_HOOK_OUTPUT) \
	$(upstart_jobs_DATA)
