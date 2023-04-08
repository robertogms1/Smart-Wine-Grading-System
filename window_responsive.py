
#na biblioteca kivy tem diversos com ponentes para criar interfaces graficas o codigo abaixo adiciona a tela e os componentes.
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class InterFace(App):
    def build(self):
        # Tamanho da tela
        Window.size = (350, 600)

        # Layout principal
        box = FloatLayout()

        # Imagem de fundo
        Fundo = Image(source='Fundo1.jpg', allow_stretch=True, keep_ratio=False)
        box.add_widget(Fundo)

        # Título
        label_title = Label(text='Insira as informações químicas do rótulo do vinho:',
                            font_size=40,
                            halign='center',
                            pos_hint={'center_x': 0.5, 'top': 0.95},
                            color=(1, 0, 0, 1),
                            size_hint=(0.9, 0.1))
        box.add_widget(label_title)

        # Álcool
        label_alcool = Label(text='Álcool:',
                             font_size=30,
                             pos_hint={'left': 0.1, 'top': 0.85},
                             color=(0, 0, 1, 1),
                             size_hint=(0.2, 0.05))
        box.add_widget(label_alcool)
        entrada_alcool = TextInput(multiline=False,
                                   font_size=30,
                                   pos_hint={'x': 0.3, 'top': 0.85},
                                   size_hint=(0.5, 0.05))
        box.add_widget(entrada_alcool)

        # pH
        label_Ph = Label(text='pH:',
                          font_size=30,
                          pos_hint={'left': 0.1, 'top': 0.75},
                          color=(0, 0, 1, 1),
                          size_hint=(0.2, 0.05))
        box.add_widget(label_Ph)
        entrada_Ph = TextInput(multiline=False,
                                font_size=30,
                                pos_hint={'x': 0.3, 'top': 0.75},
                                size_hint=(0.5, 0.05))
        box.add_widget(entrada_Ph)

        # Acidez total
        label_acidez = Label(text='Acidez:',
                          font_size=30,
                          pos_hint={'left': 0.1, 'top': 0.65},
                          color=(0, 0, 1, 1),
                          size_hint=(0.2, 0.05))
        box.add_widget(label_acidez)
        entrada_acidez = TextInput(multiline=False,
                                font_size=30,
                                pos_hint={'x': 0.3, 'top': 0.65},
                                size_hint=(0.5, 0.05))
        box.add_widget(entrada_acidez)

        # Açucar Residual
        label_acucar = Label(text='Açucar Residual:',
                          font_size=30,
                          pos_hint={'left': 0.1, 'top': 0.55},
                          color=(0, 0, 1, 1),
                          size_hint=(0.2, 0.05))
        box.add_widget(label_acucar)
        entrada_acucar = TextInput(multiline=False,
                                font_size=30,
                                pos_hint={'x': 0.3, 'top': 0.55},
                                size_hint=(0.5, 0.05))
        box.add_widget(entrada_acucar)

        #botao de enviar       
        button= Button(text='Enviar', font_size=30, pos_hint={'center_x': 0.5, 'top': 0.3}, size_hint=(0.15, 0.10),color=(0, 0, 139, 1),background_color = (0, 1, 1, 1))
        box.add_widget(button)

        return box
InterFace().run()
