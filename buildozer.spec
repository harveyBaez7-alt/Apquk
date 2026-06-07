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

# CONGELACIÓN DE VERSIONES (Para evitar el error de licencias)
android.api = 33
android.minapi = 24
android.ndk = 25b
android.build_tools_version = 33.0.0
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
