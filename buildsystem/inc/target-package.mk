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
# Copyright 2017 DFT project (http://www.firmwaretoolkit.org).
# All rights reserved. Use is subject to license terms.
#
#
# Even if this work is a complete rewrite, it is originally derivated work based
# upon mGAR build system from OpenCSW project (http://www.opencsw.org).
#
# Copyright 2001 Nick Moffitt: GAR ports system
# Copyright 2006 Cory Omand: Scripts and add-on make modules, except where otherwise noted.
# Copyright 2008 Dagobert Michelsen (OpenCSW): Enhancements to the CSW GAR system
# Copyright 2008-2013 Open Community Software Association: Packaging content
#
#
# Contributors list :
#
#    William Bonnet     wllmbnnt@gmail.com, wbonnet@theitmakers.com
#
#

# ------------------------------------------------------------------------------
#
# Protection against multiple include
#
ifdef DFT_TARGET_PACKAGE
$(info target-package.mk has already been included)
else
DFT_TARGET_PACKAGE = 1

# Some temporary default values used to debug where where variables are initialized
SW_NAME     ?= out-of-scope
SW_VERSION  ?= out-of-scope

# ------------------------------------------------------------------------------
#
# Execute the package target script
#

do-package:
	skip_target=0 ; \
# Check if make is running at generic level or target to build level \
	if [ "$(SW_VERSION)" == "out-of-scope" ] ; then \
		skip_target=1 ; \
		true ; \
	fi; \
\
	if [ ! "x$(HOST_ARCH)" = "x$(BOARD_ARCH)" ] && [ "x$(only-native-arch)" = "x1" ] ; then \
		skip_target=1 ; \
		if [ "x$(arch-warning)" = "x1" ] ; then \
			echo "Makefile processing had to be stopped during target $@ execution. Cross compilation is not supported. " ; \
			echo "The target board is based on $(BOARD_ARCH) architecture and make is running on a $(HOST_ARCH) board." ; \
			echo "The generated binaries might be invalid or scripts could fail before reaching the end of target." ; \
			echo "Makefile will now continue and process only $(HOST_ARCH) based boards. You can get the missing binaries by running" ; \
			echo "this target again on a $(BOARD_ARCH) based host and collect by yourself the generated items." ; \
			echo "In order to generate binaries for existing architectures, you need several builders, one for each target arch." ; \
		fi ; \
	fi ; \
# Check if target should be executed even if current arch is different from target arch \
# Check if skip flag has been raised it not then do the job \
	if [ ! "x$$skip_target" = "x1" ] ; then \
		if [ -f $(COOKIE_DIR)/do-package ] ; then \
				echo " DEBUG : cookie $(COOKIE_DIR)/$@ already exist, nothing left to do for make do-package" ; \
		else \
# Create the workdir used to generate packaging scripts \
			echo " DEBUG : Je sauis dans target package" ; \
			pwd ; \
			ls -lah ; \
			mkdir $(PACKAGE_DIR)/debian ; \
			if [ "$(SW_NAME)" = "u-boot" ] ; then \
# Test if current package is a u-boot then copy template and expand variables in files copy \
				cp -fr --dereference $(DFT_BUILDSYSTEM)/templates/debian-u-boot-package/* $(PACKAGE_DIR)/debian ; \
				mv  $(PACKAGE_DIR)/debian/u-boot.install $(PACKAGE_DIR)/debian/u-boot-$(BOARD_NAME).install ; \
				mv  $(PACKAGE_DIR)/debian/u-boot.postinst $(PACKAGE_DIR)/debian/u-boot-$(BOARD_NAME).postinst ; \
				mv  $(PACKAGE_DIR)/debian/u-boot.postrm $(PACKAGE_DIR)/debian/u-boot-$(BOARD_NAME).postrm ; \
				mv  $(PACKAGE_DIR)/debian/u-boot.preinst $(PACKAGE_DIR)/debian/u-boot-$(BOARD_NAME).preinst ; \
				mv  $(PACKAGE_DIR)/debian/u-boot.postrm $(PACKAGE_DIR)/debian/u-boot-$(BOARD_NAME).postrm ; \
				cp -frv --dereference $(PWD)/files $(PACKAGE_DIR)/doc ; \
			fi ; \
# Test if current package is a linux kernel then copy template and expand variables in files copy\
			if [ "$(SW_NAME)" = "linux" ] ; then \
				cp -fr --dereference $(DFT_BUILDSYSTEM)/templates/debian-linux-kernel-package/* $(PACKAGE_DIR)/debian ; \
				mv  $(PACKAGE_DIR)/debian/linux-kernel.install $(PACKAGE_DIR)/debian/linux-kernel-$(BOARD_NAME).install ; \
				mv  $(PACKAGE_DIR)/debian/linux-kernel.preinst $(PACKAGE_DIR)/debian/linux-kernel-$(BOARD_NAME).preinst ; \
				mv  $(PACKAGE_DIR)/debian/linux-kernel.postinst $(PACKAGE_DIR)/debian/linux-kernel-$(BOARD_NAME).postinst ; \
				mv  $(PACKAGE_DIR)/debian/linux-kernel.prerm $(PACKAGE_DIR)/debian/linux-kernel-$(BOARD_NAME).prerm ; \
				mv  $(PACKAGE_DIR)/debian/linux-kernel.postrm $(PACKAGE_DIR)/debian/linux-kernel-$(BOARD_NAME).postrm ; \
			fi ; \
# Expand variables in package workdir files copied from template \
			if [ "$(DEBEMAIL)" = "" ] ; then \
				find $(PACKAGE_DIR)/debian -type f | xargs sed -i -e "s/__MAINTAINER_EMAIL__/unknown/g" ; \
			else \
				find $(PACKAGE_DIR)/debian -type f | xargs sed -i -e "s/__MAINTAINER_EMAIL__/$(DEBEMAIL)/g" ; \
			fi ; \
			if [ "$(DEBFULLNAME)" = "" ] ; then \
				find $(PACKAGE_DIR)/debian -type f | xargs sed -i -e "s/__MAINTAINER_NAME__/unknown/g" ; \
			else \
				find $(PACKAGE_DIR)/debian -type f | xargs sed -i -e "s/__MAINTAINER_NAME__/$(DEBFULLNAME)/g" ; \
			fi ; \
			find $(PACKAGE_DIR)/debian -type f | xargs sed -i -e "s/__SW_VERSION__/$(SW_VERSION)/g" \
										  -e "s/__BOARD_NAME__/$(BOARD_NAME)/g" \
										  -e "s/__DATE__/$(shell LC_ALL=C date +"%a, %d %b %Y %T %z")/g" ; \
# Copy files to install into package directory (still under work tree) \
			cp -frv $(INSTALL_DIR)/* $(PACKAGE_DIR) ; \
# Go into package definition directory then create package source tarball into parent directory\
			cd $(PACKAGE_DIR) ; \
			if [ "$(SW_NAME)" = "linux" ] ; then \
				tar cfz ../$(SW_NAME)-kernel-$(BOARD_NAME)_$(SW_VERSION).orig.tar.gz * ; \
			else \
				tar cfz ../$(SW_NAME)-$(BOARD_NAME)_$(SW_VERSION).orig.tar.gz * ; \
			fi ; \
			$(DEBUILD_ENV) $(DEBUILD) $(DEBUILD_ARGS) ; \
		fi ; \
	fi ;
	$(TARGET_DONE)

do-repackage:
	@if [ -f $(COOKIE_DIR)/do-package ]  ; then
		rm -f $(COOKIE_DIR)/do-package ;
	fi ;
	$(TARGET_DONE)

# ------------------------------------------------------------------------------
#
# Create the Debian package
#

package: install pre-package do-package post-package
	$(DISPLAY_COMPLETED_TARGET_NAME)
	$(TARGET_DONE)


# ------------------------------------------------------------------------------
#
# Execute once again the package target
#

repackage: install pre-repackage do-repackage package post-repackage
	@rm -f $(COOKIE_DIR)/package
	$(DISPLAY_COMPLETED_TARGET_NAME)
	$(TARGET_DONE)

# Match initial ifdef DFT_TARGET_PACKAGE
endif
