#/***************************************************************************
# XyTools
# 
# Tools for managing tabular data with x y columns
#                             -------------------
#        begin                : 2011-08-19
#        copyright            : (C) 2011 by webmapper
#        email                : richard@webmapper.net
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

PLUGINNAME = xytools

# for building dist zip
TEMPDIR = /tmp

PY_FILES = xytools.py xytoolsdialog.py xytools_fieldchooserdialog.py utils.py __init__.py

EXTRAS = icon.png help.png metadata.txt

DOCS = docs/*

UI_FILES = ui_xytools.py ui_field_chooser.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)
	rst2html docs/index.rst > docs/index.html

%.py : %.rc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis2/python/plugins
deploy: compile
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vrf $(PY_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)/providers
	cp -vrf providers/*.py $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)/providers
	cp -vf $(UI_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vrf $(EXTRAS) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)/docs
	cp -vrf $(DOCS) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)/docs/



dist: cleandist deploy
	mkdir -p $(TEMPDIR)/$(PLUGINNAME)
	cp -r * $(TEMPDIR)/$(PLUGINNAME)
	cd $(TEMPDIR); zip -9rv $(PLUGINNAME).zip $(PLUGINNAME) -i \*.py \*.html \*.png \*.txt
	@echo "You can find the plugin for the qgis repo here: $(TEMPDIR)/$(PLUGINNAME).zip"

cleandist:
	rm -rf $(TEMPDIR)/$(PLUGINNAME)
	rm -rf $(TEMPDIR)/$(PLUGINNAME).zip
