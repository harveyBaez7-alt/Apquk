[app]
title = NeoLauncherAR
package.name = neolauncherar
package.domain = org.cyberpunk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pyjnius,pillow
orientation = landscape
android.permissions = CAMERA, BODY_SENSORS

# ADECUACIÓN AL ENTORNO EXISTENTE EN GITHUB (API Antigua)
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools_version = 31.0.0
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
