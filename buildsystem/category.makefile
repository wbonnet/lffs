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
# Copyright 2019 DFT project (http://www.debianfirmwaretoolkit.org).
# All rights reserved. Use is subject to license terms.
#
#
# Contributors list :
#
#    William Bonnet     wllmbnnt@gmail.com, wbonnet@theitmakers.com
#

buildsystem := ../../../buildsystem

# Do not recurse the following subdirs
MAKE_FILTERS  = Makefile README.md .
CATEGORIES    = laptop desktop set-top-box single-board-computer
SW_NAME       = SW_NAME_undefined_at_category_level

# ------------------------------------------------------------------------------
#
# Targets not associated with a file (aka PHONY)
#
.PHONY: help sanity-check

sanity-check :
# Board category directory contains several folders, on per board in this category
# Each board folder must contain a board.mk file with board specific information, 
# a mandatory kernel folder, optional folders like u-boot for boot loader and files 
# to store needed additionnal files
	@for board in $(shell find . -mindepth 1 -maxdepth 1 -type d ) ; do \
		if [ ! -e "$$board/Makefile" ] ; then \
			echo "Makefile in $(shell pwd)/$$board is Missing. It should be a symlink to  $(buildsystem)/board.makefile" ; \
			echo "You can fix with the following shell commands :" ; \
			echo "git rm -f $$board/Makefile" ; \
			echo "ln -s $(buildsystem)/board.makefile $(shell pwd)/$$board/Makefile" ; \
			echo "git add $$board/Makefile" ; \
			echo "exit 101101" ; \
			exit 1 ; \
		fi ; \
		s=`readlink $$board/Makefile` ; \
		if [ !  "$$s" = "$(buildsystem)/board.makefile" ] ; then \
			echo "Makefile symlink in $$board must link to $(buildsystem)/board.makefile" ; \
			echo "It targets to $$s" ; \
			echo "exit 825" ; \
			exit 1 ; \
		fi ; \
		if [ ! -f $$board/board.mk ] ; then \
			echo "Board description file board.mk is missing in directory $(shell pwd)/$$board" ; \
			echo "You can fix with the following shell commands :" ; \
			echo "git rm -f $$board/Makefile" ; \
			echo "cp  $(buildsystem)/board.mk.template $(shell pwd)/$$board/board.mk" ; \
			echo "git add $(shell pwd)/$$board/board.mk" ; \
			echo "Warning !!! : Don't forget to edit this file and replace 'unkown' values with board specific values" ; \
			echo "exit 191117-01" ; \
			exit 1 ; \
		fi ; \
	done ; \
	for folder in $(shell find . -mindepth 1 -maxdepth 1 -type d ) ; do \
		echo "tring folder $$folder" ; \
		$(MAKE) -C $$folder sanity-check || exit 1 ; \
		echo "make sanity-check in folder $$folder" ; \
	done ;

# Catch all target. Call the same targets in each subfolder
%:
	@for i in $(filter-out $(MAKE_FILTERS),$(shell find . -maxdepth 1 -type d )) ; do \
		echo "avant le make du catch all" ; \
		$(MAKE) -C $(i) $* || exit 1 ; \
	done

# ------------------------------------------------------------------------------
#
# Target that prints the help
#
help :
	@echo "The target given to make will be called recursively on each board folder."