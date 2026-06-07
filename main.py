import time
from kivymd.app import MDApp
from jnius import autoclass  # Conecta Python con el hardware de Android
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window

# Vincular componentes nativos de Android para sensores
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
Sensor = autoclass('android.hardware.Sensor')
SensorManager = autoclass('android.hardware.SensorManager')

class LauncherFusionLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Forzar orientaciÃ³n horizontal para el visor
        Window.rotation = 90
        
        self.cursor_x = Window.width / 2
        self.cursor_y = Window.height / 2
        self.sensibilidad = 400.0  
        
        # Variables para el Autoclic por permanencia (Dwell Click)
        self.ultima_x_inmovil = self.cursor_x
        self.ultima_y_inmovil = self.cursor_y
        self.tiempo_quieto = 0
        self.umbral_movimiento = 20
        self.ventana_seleccionada = None

        # Fondo del lienzo (Mapeado para la cÃ¡mara en compilaciÃ³n)
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1) 
            self.bg_rect = Rectangle(pos=(0,0), size=(Window.width, Window.height))
            
        # Ventanas flotantes traslÃºcidas (60% de opacidad)
        self.btn_youtube = Button(
            text="YOUTUBE VIRTUAL",
            size_hint=(None, None),
            size=(300, 200),
            pos=(100, 200),
            background_color=(1, 0, 0, 0.6) 
        )
        
        self.btn_escritorio = Button(
            text="ESCRITORIO TRABAJO",
            size_hint=(None, None),
            size=(300, 200),
            pos=(500, 200),
            background_color=(0, 0.4, 1, 0.6) 
        )
        
        self.add_widget(self.btn_youtube)
        self.add_widget(self.btn_escritorio)
        
        # Texto informativo superior
        self.lbl_estado = Label(
            text="Mira fijamente una ventana 1.5s para arrastrarla.\nGiro rÃ¡pido: Izquierda = Home",
            pos_hint={'center_x': 0.5, 'top': 0.95},
            color=(0, 1, 0.8, 1)
        )
        self.add_widget(self.lbl_estado)
        
        # Dibujo del cursor central (Punto de mira)
        with self.canvas.after:
            self.color_cursor = Color(0, 1, 0.5, 1) 
            self.cursor_mesh = Ellipse(pos=(self.cursor_x, self.cursor_y), size=(20, 20))

        self.inicializar_sensores_android()
        Clock.schedule_interval(self.actualizar_sistema, 1.0 / 60.0)

    def inicializar_sensores_android(self):
        try:
            activity = PythonActivity.mActivity
            self.sensorManager = activity.getSystemService(Context.SENSOR_SERVICE)
            self.giroscopio = self.sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
            
            # Listener para capturar el movimiento de la cabeza
            self.sensorListener = autoclass('android.hardware.SensorEventListener')
            self.sensorManager.registerListener(self.sensorListener, self.giroscopio, SensorManager.SENSOR_DELAY_GAME)
        except Exception:
            self.lbl_estado.text = "Modo de simulaciÃ³n de escritorio activado"

    def actualizar_sistema(self, dt):
        distancia_movida = abs(self.cursor_x - self.ultima_x_inmovil) + abs(self.cursor_y - self.ultima_y_inmovil)
        
        if distancia_movida > self.umbral_movimiento:
            self.ultima_x_inmovil = self.cursor_x
            self.ultima_y_inmovil = self.cursor_y
            self.tiempo_quieto = 0
        else:
            self.tiempo_quieto += dt
            if self.tiempo_quieto >= 1.5:  
                self.ejecutar_autoclic()
                self.tiempo_quieto = 0

        if self.ventana_seleccionada:
            self.ventana_seleccionada.pos = (self.cursor_x - 150, self.cursor_y - 100)

        self.cursor_mesh.pos = (self.cursor_x - 10, self.cursor_y - 10)

    def ejecutar_autoclic(self):
        if self.ventana_seleccionada:
            self.ventana_seleccionada = None
            self.lbl_estado.text = "Ventana fijada en el espacio virtual."
        else:
            if self.btn_youtube.collide_point(self.cursor_x, self.cursor_y):
                self.ventana_seleccionada = self.btn_youtube
                self.lbl_estado.text = "Sujetando: YouTube Virtual"
            elif self.btn_escritorio.collide_point(self.cursor_x, self.cursor_y):
                self.ventana_seleccionada = self.btn_escritorio
                self.lbl_estado.text = "Sujetando: Escritorio de Trabajo"

class LauncherApp(MDApp):
    def build(self):
        return LauncherFusionLayout()

if __name__ == '__main__':
    LauncherApp().run()
