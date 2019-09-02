# vim: ft=make ts=4 sw=4 noet
#
# The contents of this file are subject to the Apache 2.0 license you may not
# use this file except in compliance with the License.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
#
# Copyright 2016 DFT project (http://www.debianfirmwaretoolkit.org).
# All rights reserved. Use is subject to license terms.
#
#
# Contributors list :
#
#    William Bonnet     wllmbnnt@gmail.com, wbonnet@theitmakers.com
#
#

# Include the board definition
include board.mk

# Defines the software version
PACKAGE_DATE = $(shell LC_ALL=C date +"%a, %d %b %Y %T %z")
PACKAGE_DATE = $(shell date )
FILTER_DIRS  = files/
HOST_ARCH    = $(shell uname -m)

# Defines relative path to root of the buildsystem tree
DFT_HOME     = ../../../../..

# ------------------------------------------------------------------------------
#
# Targets not associated with a file (aka PHONY)
#
.PHONY: help

# Create a new board entry in the repository
new-version:
	@if [ -d "./$(VERSION)" ] ; then \
		echo ". Version $(VERSION) already exist. Doing nothing..." ; \
	else  \
		echo ". Creating the directory structure for version $(VERSION)" ; \
		mkdir -p $(VERSION) ; \
		cd $(VERSION) ; \
		cp -f $(DFT_HOME)/buildsystem/templates/u-boot-version.makefile Makefile ; \
		ln -s $(DFT_HOME)/buildsystem/ buildsystem ; \
		mkdir -p files ; \
		touch files/.gitkeep ; \
		ln -s ../../files/install.u-boot.$(BOARD_NAME).md ./files/ ; \
		mkdir -p patches ; \
		touch patches/.gitkeep ; \
		echo "work-$(BOARD_NAME)/" > .gitignore ; \
		sed -i -e "s/__UBOOT_VERSION__/$(VERSION)/g" Makefile ; \
		cp -fr $(DFT_HOME)/buildsystem/templates/debian.u-boot debian ; \
		cd debian ; \
		mv u-boot.install u-boot-$(BOARD_NAME).install ; \
		cd ../.. ; \
		find $(VERSION)/debian -type f | xargs sed -i -e "s/__UBOOT_VERSION__/$(VERSION)/g" \
	                                         -e "s/__BOARD_NAME__/$(BOARD_NAME)/g" \
	                                         -e "s/__DATE__/$(shell LC_ALL=C date +"%a, %d %b %Y %T %z")/g" ; \
        if [ "${DEBEMAIL}" = "" ] ; then \
			find $(VERSION)/debian -type f | xargs sed -i -e "s/__MAINTAINER_EMAIL__/unknown/g" ; \
		else \
			find $(VERSION)/debian -type f | xargs sed -i -e "s/__MAINTAINER_EMAIL__/${DEBEMAIL}/g" ; \
		fi ; \
		if [ "${DEBFULLNAME}" = "" ] ; then \
			find $(VERSION)/debian -type f | xargs sed -i -e "s/__MAINTAINER_NAME__/unknown/g" ; \
		else \
			find $(VERSION)/debian -type f | xargs sed -i -e "s/__MAINTAINER_NAME__/${DEBFULLNAME}/g" ; \
		fi ; \
		git add $(VERSION) ; \
	fi ;

# Call clean and dist clean targets in subfolders
clean:
fetch:
distclean:
	@for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
	$(MAKE) -C $$i $* || exit 1 ; \
	done 

# Catch all target. Call the same targets in each subfolder
%:
	@if [ ! "x$(HOST_ARCH)" = "x$(BOARD_ARCH)" ] ; \
	then \
	    echo "board is $(BOARD_ARCH) and i run on $(HOST_ARCH). Skipping recursive target call..." ; \
	    true ; \
	else \
		for i in $(filter-out $(FILTER_DIRS),$(wildcard */)) ; do \
			$(MAKE) -C $$i $* || exit 1 ; \
		done \
	fi

# ------------------------------------------------------------------------------
#
# Target that prints the help
#
help :
	@echo "Available targets are :"
	@echo '   new-version VERSION=YYYY.MM Create a new version entry. ex: make new-version VERSION=2019.07'
	@echo '                               This target will create a subdirectory named after the content of the VERSION variable.'
	@echo '                               It will contain the Makefile and all the files needed to fetch and build the given'
	@echo '                               version. It also instanciate Debian package template.'