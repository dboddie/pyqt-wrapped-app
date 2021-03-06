#!/usr/bin/env python

"""
main.py - Equivalent main program to the one in the main.cpp file.

Copyright (C) 2013 David Boddie <david.boddie@met.no>

This file is part of the pyqt-wrapped-app example.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
from PyQt4.QtGui import QApplication
from wrapped_app import MainWindow

from logindialog import PyLoginDialog

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    login_dialog = PyLoginDialog()
    window.setLoginDialog(login_dialog)
    window.show()
    sys.exit(app.exec_())
