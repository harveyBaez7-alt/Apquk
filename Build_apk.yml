name: Compilar APK Nativo Android

on:
  push:
    branches:
      - main
      - master
  workflow_dispatch: # Esto te permite activar la compilaciÃ³n manualmente con un botÃ³n en la web de GitHub

jobs:
  build:
    name: Compilar APK
    runs-on: ubuntu-latest

    steps:
      # 1. Descargar el cÃ³digo de tu repositorio
      - name: Checkout del cÃ³digo
        uses: actions/checkout@v4

      # 2. Configurar la versiÃ³n correcta de Java (JDK 17 es el estÃ¡ndar actual)
      - name: Configurar Java JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      # 3. Darle permisos de ejecuciÃ³n al script de Gradle en el servidor virtual
      - name: Otorgar permisos a Gradle Wrapper
        run: chmod +x ./gradlew

      # 4. Ejecutar la compilaciÃ³n nativa en modo de depuraciÃ³n/prueba (Debug)
      - name: Compilar con Gradle
        run: ./gradlew assembleDebug

      # 5. Subir la APK generada a la web de GitHub para descargarla
      - name: Guardar APK como Artefacto Descargable
        uses: actions/upload-artifact@v4
        with:
          name: app-debug-apk
          path: app/build/outputs/apk/debug/app-debug.apk
