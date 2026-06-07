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

# Estas versiones existen físicamente dentro del servidor de GitHub:
android.api = 34
android.minapi = 24
android.build_tools_version = 34.0.0
android.ndk = 26b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
