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
# Debian Firmware Toolkit is the new name of Linux Firmware From Scratch
# Copyright 2014 LFFS project (http://www.linuxfirmwarefromscratch.org).
#
#
# Contributors list :
#
#    William Bonnet     wllmbnnt@gmail.com, wbonnet@theitmakers.com
#
#

""" This modules implements the functionnalities used to create the initramfs in charge of
setting up the firmware in memory at system boot.
"""

import logging
import os
import stat
import tempfile
import datetime
import tarfile
from dft.cli_command import CliCommand
from dft.model import Key


#
#    Class BuildFirmwareUpdate
#
class BuildFirmwareUpdate(CliCommand):
  """This class implements method needed to create the archives containing
  firmware update, and all the scripts needed at deployment.

  """

  # -------------------------------------------------------------------------
  #
  # __init__
  #
  # -------------------------------------------------------------------------
  def __init__(self, dft, project):
    """Default constructor
    """

    # Initialize ancestor
    CliCommand.__init__(self, dft, project)

    # Tar archive object
    tar = None



  # -------------------------------------------------------------------------
  #
  # build_update_archive
  #
  # -------------------------------------------------------------------------
  def build_update_archive(self):
    """This method generates the final archive containing the elements of the
    firmware. The main steps :
    . Creating a manisfest describing the content items (hash value)
    . Creat a tar file, containing all the data from the content subirectory
    . Create a detached signature using either gnupg or openssl

    The two generated files are stored under firmware (same levelas content)
    """

    # Check that there is a firmware configuration file first
    if self.project.firmware is None:
      self.project.logging.critical("The firmware configuration file is not defined in \
                                     project file")
      exit(1)

    # Check that the target files and directories exists
    if not os.path.isdir(self.project.get_firmware_content_directory()):
      self.project.logging.critical("The firmware directory does not exist. Did you forget to run \
                                     assemble_firmwarec command before ? Expected directory is " + \
                                     self.project.get_firmware_content_directory())
      exit(1)



    # Create the tar archive
    self.create_main_archive()

    # Sign the main archive
    self.sign_main_archive()

    # And we are done
    return

  # -------------------------------------------------------------------------
  #
  # create_main_archive
  #
  # -------------------------------------------------------------------------
  def create_main_archive(self):
    """This method create the manifest of the archive (a file listing all the
    files with their checksums). Then it creates the archive to be signed.

    All the files are stored under firmware directory. In the en only two
    files should be produced. The archive, created by this method, and the
    detached signature. Coded in next method.
    """

    # Output current task to logs
    logging.info("Creating the main archive")

    # Creating the manifest

    # Creating the archive
    dest_archive = self.project.get_firmware_output_directory()
    dest_archive += "/" + self.project.firmware[Key.CONFIGURATION.value][Key.FILENAME.value]

    # Create the tar itself
    self.tar = tarfile.open(name=dest_archive, mode='w')

    # Iterate firmware content directory
    for name in os.listdir(self.project.get_firmware_content_directory()):
      # And add each and every file
      self.tar.add(name)

    # Let's close the tar to flushit
    self.tar.close()



  # -------------------------------------------------------------------------
  #
  # sign_main_archive
  #
  # -------------------------------------------------------------------------
  def sign_main_archive(self):
    """This method does a digital signature of the archive, or a hash (should
    not be used). Depending on configuration, it ca use either a hash function
    such as sha1sum, or a signature software such as gnupg or openssl.
    """

    # Output current task to logs
    logging.info("Signin the main archive")