
%.conf: %.conf.in Makefile
	$(AM_V_GEN) $(SED) -e 's^\@pkgdatadir\@^$(pkgdatadir)^g' < $< > $@
