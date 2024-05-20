[app]
# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mainapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = kivy

# (str) Application build tool
build_mode = debug

[buildozer]
# (list) List of source files
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png,*.jpg,*.kv

# (list) List of exclusions using pattern matching
source.exclude_patterns = license.txt,README.md,.git,buildozer.spec

# (str) Path to a custom buildozer.spec template (relative to the main directory)
buildozer.spec.template = templates/buildozer.spec

# (int) Port to use for the web server for debug apk - 0 to disable
port = 0

# (str) Log level (debug, info, warning, error, critical)
log_level = 2

# (str) Display warning if buildozer is run as root (0, 1, on, off)
warn_on_root = 1
