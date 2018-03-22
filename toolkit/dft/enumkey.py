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


""" This module contains the definition of all the string constants used by
DFT configuration files. A dictionary of strings is built in order to handle
case such as the need of modification of a string without modifying all
occurences in the code.
"""

from enum import Enum

# -----------------------------------------------------------------------------
#
# class Key
#
# -----------------------------------------------------------------------------
class Key(Enum):
  """This class defines the valid keys to used to access infrmation from
  confiugration files. The keys are enumerated vlues defined by string. The string
  used are (understand 'must be') the same as the keys in yaml files.

  No string should be manipulated directly, only enum values
  """

  # Define each and every key and associated string used in the DFT tool

  ABSENT = "absent"
  ACTION = "action"
  ADDITIONAL_BINARIES = "additional_binaries"
  ADDITIONAL_MODULES = "additional_modules"
  ADDITIONAL_ROLES = "additional_roles"
  ALIGNMENT = "alignment"
  ALL_ROOT = "all_root"
  ALLOW_OPTIONAL = "allow_optional"
  ALLOWED = "allowed"
  ALLOWED_ARCH = "allowed_arch"
  ALLOWED_VERSION = "allowed_version"
  ANTIVIRUS = "antivirus"
  ARCH = "arch"
  ARCHITECTURE = "architecture"
  ARCHITECTURES = "architectures"
  ARCHIVE_FILENAME_EXTENSION = ".tar"
  ARGUMENTS = "arguments"
  ARM = "arm"
  ARMBIAN = "armbian"
  ARMBIAN_SIGNING_PUBKEY = "9F0E78D5"
  ARMEL = "armel"
  ARMHF = "armhf"
  ARMWIZARD = "armwizard"
  ARMWIZARD_SIGNING_PUBKEY = "1B362699"
  ASSEMBLE_FIRMWARE = "assemble_firmware"
  AUFS = "aufs"
  BANK_0 = "bank_0"
  BANK_1 = "bank_1"
  BLACKLISTED_ARCH = "blacklisted_arch"
  BLACKLISTED_VERSION = "blacklisted_version"
  BLOCK_SIZE = "block_size"
  BOARD = "board"
  BOOTCHAIN = "bootchain"
  BOOTCHAIN_WORKDIR = "bootchain"
  BSP = "bsp"
  BSP_BASE = "bsp_base"
  BSP_FILE = "bsp_file"
  BUILD_FIRMWARE = "build_firmware"
  BUILD_FIRMWARE_UPDATE = "build_firmware_update"
  BUILD_IMAGE = "build_image"
  BUILD_PARTITIONS = "build_partitions"
  BUILD_ROOTFS = "build_rootfs"
  BUILDING_SEQUENCES = "building_sequences"
  CHECK = "check"
  CHECK_ROOTFS = "check_rootfs"
  COMPRESSION = "compression"
  COMPRESSION_OPTIONS = "compression_options"
  COMPRESSOR = "compressor"
  CONFIG_FILE = "config_file"
  CONFIGURATION = "configuration"
  CONTENT = "content"
  CONTENT_ANTIVIRUS = "content_antivirus"
  CONTENT_FILES = "content_files"
  CONTENT_INFO = "content_information"
  CONTENT_INFORMATION = "content_information"
  CONTENT_PACKAGES = "content_packages"
  CONTENT_PARTITION_MAPPING = "install_content_partition_mapping"
  CONTENT_ROOTKIT = "content_rootkit"
  CONTENT_SECURITY = "content_security"
  CONTENT_VULNERABILITIES = "content_vulnerabilities"
  CONTENT_WORKDIR = "content"
  CSV = "csv"
  CUSTOM = "custom"
  DEBIAN = "debian"
  DEBOOTSTRAP_REPOSITORY = "debootstrap_repository"
  DEBOOTSTRAP_TARGET = "minbase"
  DEFAULT_CONFIGURATION_FILE = "~/.dftrc"
  DEFAULT_PROJECT_FILE = "project.yml"
  DEFAULT_SEQUENCE_NAME = "__dft_default_sequence__"
  DESCRIPTION = "description"
  DEVICE_NUMBER = "device_number"
  DEVICE_PARTITION = "device_partition"
  DEVICE_TYPE = "device_type"
  DEVICES = "devices"
  DEVUAN = "devuan"
  DEVUAN_SIGNING_PUBKEY = "FA1B0274"
  DFT_BASE = "dft_base"
  DIRECTORIES = "directories"
  DIRECTORY = "directory"
  DISTRIBUTIONS = "distributions"
  DUAL_BANKS = "dual_banks"
  DUMP = "dump"
  EMPTY = "empty"
  EXPECTED_RESULT = "expected_result"
  EXT_FS_TUNE = "ext_fs_tune"
  EXTENDED = "extended"
  FAILOVER = "failover"
  FILE = "file"
  FILENAME = "filename"
  FILENAME_SUFFIX = "filename_suffix"
  FILENAME_TIMESTAMP = "filename_timestamp"
  FILENAME_TIMESTAMP_FORMAT = "filename_timestamp_format"
  FILES = "files"
  FILESYSTEM = "filesystem"
  FILESYSTEMS = "filesystems"
  FILL_METHOD = "fill_method"
  FIRMWARE = "firmware"
  FIRMWARE_FILENAME_EXTESION = ".fw"
  FIRMWARE_WORKDIR = "firmware"
  FLAGS = "flags"
  FORBIDDEN = "forbidden"
  FORCE_UID = "force_uid"
  FORMAT = "format"
  GENERATE_BOOTSCR = "generate_bootscr"
  GENERATE_DEB = "generate_deb"
  GENERATE_SRC = "generate_src"
  GENERATE_VALIDITY_CHECK = "generate_validity_check"
  GPG_ARMOR_SIGNATURE = "gpg_armor_signature"
  GPG_KEY = "gpg_key"
  GPG = "gpg"
  GPG2 = "gpg2"
  GROUP = "group"
  GRUB = "grub"
  HASH_METHOD = "hash_method"
  IMAGE = "image"
  IMAGE_WORKDIR = "image"
  INIT_FILENAME = "init_filename"
  INITRAMFS = "initramfs"
  INSTALL_BOOTCHAIN = "install_bootchain"
  INSTALL_MISSING_SOFTWARE = "install_missing_software"
  INSTALL_MSSING_SOFTWARE = "install_mssing_software"
  INSTALLATION = "installation"
  INSTALLATION_CONSTRAINT = "installation_constraint"
  INSTALLED_SIZE = "installed_size"
  JSON = "json"
  KEEP_BOOTSTRAP_FILES = "keep_bootstrap_files"
  KEEP_ROOTFS_HISTORY = "keep_rootfs_history"
  KEEP_SOURCE = "keep_source"
  KERNEL = "kernel"
  LABEL = "label"
  LABEL_RESULT_FAIL = "[FAIL]"
  LABEL_RESULT_OK = "[ OK ]"
  LAYOUT = "layout"
  LOG_LEVEL = "log_level"
  LOG_LEVEL_INFO = "INFO"
  LOGICAL = "logical"
  LYNIS = "lynis"
  MANDATORY = "mandatory"
  MANDATORY_ONLY = "mandatory_only"
  MAX_VERSION = "max_version"
  MD5 = "md5"
  MESSAGE_END = "message_end"
  MESSAGE_START = "message_start"
  METHOD = "method"
  MIN_VERSION = "min_version"
  MODE = "mode"
  MOUNT_OPTIONS = "mount_options"
  MOUNTPOINT = "mountpoint"
  NAME = "name"
  NATIVE = "__native__"
  NO_CONSTRAINT = "no_constraint"
  NO_DATABLOCK_COMPRESSION = "no_datablock_compression"
  NO_DUPICATE_CHECK = "no_dupicate_check"
  NO_EXPORTS = "no_exports"
  NO_FRAGMENTBLOCK_COMPRESSION = "no_fragmentblock_compression"
  NO_INODE_COMPRESSION = "no_inode_compression"
  NO_SPARE = "no_spare"
  NO_XATTRS_COMPRESSION = "no_xattrs_compression"
  NOPAD = "nopad"
  OPENSSL = "openssl"
  OPT_CONFIG_FILE = "--config-file"
  OPT_CONTENT_ANTIVIRUS = "--generate-antivirus-information"
  OPT_CONTENT_FILES = "--generate-files-information"
  OPT_CONTENT_PACKAGES = "--generate-packages-information"
  OPT_CONTENT_ROOTKIT = "--generate-rootkit-information"
  OPT_CONTENT_SECURITY = "--generate-security-information"
  OPT_CONTENT_VULNERABILITIES = "--generate-vulnerabilities-information"
  OPT_HELP_LABEL = "Command to execute"
  OPT_KEEP_BOOTSTRAP_FILES = "--keep-bootstrap-files"
  OPT_LOG_LEVEL = "--log-level"
  OPT_OVERRIDE_DEBIAN_MIRROR = "--override-debian-mirror"
  OPT_PROJECT_FILE = "--project"
  OPT_SEQUENCE_NAME = "--sequence"
  OPTIONS = "options"
  ORIGIN = "origin"
  OUTPUT = "output"
  OUTPUT_PKG_ARCHITECTURE = "output_pkg_architecture"
  OUTPUT_PKG_DESCRIPTION = "output_pkg_description"
  OUTPUT_PKG_INSTALLED_SIZE = "output_pkg_installed_size"
  OUTPUT_PKG_MD5 = "output_pkg_md5"
  OUTPUT_PKG_NAME = "output_pkg_name"
  OUTPUT_PKG_SHA256 = "output_pkg_sha256"
  OUTPUT_PKG_SIZE = "output_pkg_size"
  OUTPUT_PKG_STATUS = "outpuat_pkg_status"
  OUTPUT_PKG_VERSION = "output_pkg_version"
  OVERLAYFS = "overlayfs"
  OVERRIDE_DEBIAN_MIRROR = "override_debian_mirror"
  OWNER = "owner"
  PACKAGE = "package"
  PACKAGES = "packages"
  PARTITION = "partition"
  PARTITIONS = "partitions"
  PASS = "pass"
  PATH = "path"
  PIN = "Pin"
  PIN_PRIORITY = "Pin-Priority"
  PINNING = "pinning"
  PRIMARY = "primary"
  PROJECT_DEFINITION = "project_definition"
  PROJECT_FILE = "project_file"
  PROJECT_NAME = "project_name"
  PROJECT_PATH = "project_path"
  PROJECT_WORKDIR = "project_base_workdir"
  PUBKEY = "pubkey"
  PUBKEY_GPG = "pubkey_gpg"
  PUBKEY_URL = "pubkey_url"
  REMOVE_DOWNLOADED_ARCHIVES = "remove_downloaded_archives"
  REMOVE_VALIDITY_CHECK = "remove_validity_check"
  REPOSITORIES = "repositories"
  RESCUE = "rescue"
  RESCUE_IMAGE = "rescue_image"
  RESERVED_SIZE = "reserved_size"
  RESILIENCE = "resilience"
  RKHUNTER = "rkhunter"
  ROLES = "roles"
  ROOTFS = "rootfs"
  ROOTFS_DIR = "rootfs"
  ROOTKIT = "rootkit"
  RUN_SEQUENCE = "run_sequence"
  SCAN = "scan"
  SECTIONS = "sections"
  SECURITY = "security"
  SEQUENCE_NAME = "sequence_name"
  SHA1 = "sha1"
  SHA224 = "sha224"
  SHA256 = "sha256"
  SHA384 = "sha384"
  SHA512 = "sha512"
  SIGNATURE = "signature"
  SIZE = "size"
  SKIP_MISSING_SOFTWARE = "skip_missing_software"
  SOURCE = "source"
  SQUASHFS = "squashfs"
  SQUASHFS_CONFIGURATION = "squashfs_configuration"
  SQUASHFS_FILE = "squashfs_file"
  STACK_DEFINITION = "stack_definition"
  STACK_ITEM = "stack_item"
  START_SECTOR = "start_sector"
  STATUS = "status"
  STDOUT = "stdout"
  STEPS = "steps"
  STRIP_ROOTFS = "strip_rootfs"
  STRIPPING = "stripping"
  SUITE = "suite"
  SYMLINK = "symlink"
  TARGET = "target"
  TARGET_PATH = "target_path"
  TARGETS = "targets"
  TMPFS = "tmpfs"
  TYPE = "type"
  UBOOT = "u-boot"
  UNIT = "unit"
  UNKNOWN = "unknown"
  UPDATE = "update"
  UPDATE_DATABASE = "update_database"
  UPDATE_PARTITION = "update_partition"
  URL = "url"
  USE_FRAGMENTS = "use_fragments"
  USE_HOST_AV = "use_host_av"
  UTF8 = "utf-8"
  VALUE = "value"
  VARIABLES = "variables"
  VERSION = "version"
  VULNERABILITIES = "vulnerabilities"
  WORKING_DIR = "working_dir"
  XATTRS = "xattrs"
  XML = "xml"
  YAML = "yaml"
  YML = "yml"
