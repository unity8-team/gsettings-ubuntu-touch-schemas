
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
	$(upstart_jobs_in) \
	$(upstart_scripts_SCRIPTS)

CLEANFILES = \
	$(upstart_jobs_DATA)
