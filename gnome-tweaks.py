#! /usr/bin/python3
# SPDX-License-Identifier: GPL-3.0+
# License-Filename: LICENSES/GPL-3.0

import gettext
import logging
import locale
import os.path
import optparse
import signal
import sys

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Handy", "0.0")

import gtweak
from gtweak.defs import VERSION


if __name__ == '__main__':
    parser = optparse.OptionParser(version=VERSION)
    parser.add_option("-t", "--test", action="store_true",
                      help="Enable test and debug code")
    parser.add_option("-l", "--load", action="store_true",
                      help="Load all tweaks")
    parser.add_option("-p", "--prefix",
                      help="Installation prefix (for gsettings schema, themes, etc)",
                      metavar="[/, /usr]")
    parser.add_option("-v", "--verbose", action="store_true",
                      help="Print the names of settings modified")
    parser.add_option("-d", "--debug", action="store_true",
                      help="Enable debug output")
    options, args = parser.parse_args()

    try:
        from gtweak.defs import GSETTINGS_SCHEMA_DIR, TWEAK_DIR, DATA_DIR, \
                                PKG_DATA_DIR, LOCALE_DIR, LIBEXEC_DIR
        _defs_present = True
    except ImportError:
        GSETTINGS_SCHEMA_DIR = TWEAK_DIR = DATA_DIR = PKG_DATA_DIR = \
                               LOCALE_DIR = LIBEXEC_DIR = ""
        _defs_present = False

    # the supplied prefix always beats the contents of defs
    if options.prefix or not _defs_present:
        _prefix = options.prefix or "/usr"
        DATA_DIR = os.path.join(_prefix, "share")
        LOCALE_DIR = os.path.join(_prefix, "share", "locale")
        GSETTINGS_SCHEMA_DIR = os.path.join(_prefix, "share", "glib-2.0", "schemas")
        _me = os.path.abspath(os.path.dirname(__file__))
        TWEAK_DIR = os.path.join(_me, "gtweak", "tweaks")
        PKG_DATA_DIR = os.path.join(_me, "data")

    gtweak.GSETTINGS_SCHEMA_DIR = GSETTINGS_SCHEMA_DIR
    gtweak.TWEAK_DIR = TWEAK_DIR
    gtweak.DATA_DIR = DATA_DIR
    gtweak.PKG_DATA_DIR = PKG_DATA_DIR
    gtweak.LOCALE_DIR = LOCALE_DIR
    gtweak.LIBEXEC_DIR = LIBEXEC_DIR
    gtweak.ENABLE_TEST = options.test
    gtweak.ALL_TWEAKS = options.load
    gtweak.APP_NAME = "gnome-tweaks"
    gtweak.VERBOSE = options.verbose

    if options.debug:
        level = logging.DEBUG
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(levelname)-8s: %(message)s", level=level)

    locale.setlocale(locale.LC_ALL, None)
    gettext.install(gtweak.APP_NAME, LOCALE_DIR, names=('gettext', 'ngettext'))

    from gtweak.app import GnomeTweaks
    app = GnomeTweaks()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    exit_status = app.run(None)
    sys.exit(exit_status)
