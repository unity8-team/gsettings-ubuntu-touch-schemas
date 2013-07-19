desktop_gschemas_in_in = \ 
	com.ubuntu.touch.network.gschema.xml.in.in \
	com.ubuntu.touch.system.gschema.xml.in.in

@INTLTOOL_XML_NOMERGE_RULE@

#gsettings_ENUM_NAMESPACE = com.ubuntu.touch
#gsettings_ENUM_FILES = $(top_srcdir)/headers/*.h

desktop_gschemas_in = $(desktop_gschemas_in_in:.xml.in.in=.xml.in)
gsettings_SCHEMAS = $(desktop_gschemas_in:.xml.in=.xml)

%.gschema.xml.in: %.gschema.xml.in.in Makefile
	$(AM_V_GEN) $(SED) -e 's^\@datadir\@^$(datadir)^g' -e 's^\@GETTEXT_PACKAGE\@^$(GETTEXT_PACKAGE)^g' < $< > $@

@GSETTINGS_RULES@

EXTRA_DIST =				\
	$(desktop_gschemas_in_in)	

CLEANFILES =					\
	$(gsettings_SCHEMAS)			\
	$(desktop_gschemas_in)			\
	*.gschema.valid

