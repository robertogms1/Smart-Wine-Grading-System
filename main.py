#na biblioteca kivy tem diversos com ponentes para criar interfaces graficas o codigo abaixo adiciona a tela e os componentes.
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
# a seguir determinamos as caracteristicas dos componentes como cor,texto,tamanho,etc...
class InterFace(App):
    def build(self):
#Tela do App
        box= FloatLayout()
# Adiciona a imagem como widget de fundo
        Fundo = Image(source='Fundo.jpg', allow_stretch=True, keep_ratio=False)
        box.add_widget(Fundo)
#informação titulo
        label_title=Label(text='Insira as informações químicas do rótulo do vinho:', font_size=20, halign='center', pos_hint={'center_x': 0.5, 'top': 1.4}, color=(1, 0, 0, 1))
        box.add_widget(label_title)
#informação de entrada
        label_alcool=Label(text='Álcool:', font_size=16, pos_hint={'right': 0.4, 'top': 0.7}, size_hint=(0.2, 0.05),color=(0, 0, 1, 1))
        box.add_widget(label_alcool)
#caixa de entrada onde o usuario digita as informaçoes neste caso alcool
        entrada_alcool=TextInput(multiline=False, font_size=16, pos_hint={'center_x': 0.5, 'top': 0.7}, size_hint=(0.3, 0.05))
        box.add_widget(entrada_alcool)
#botão de enviar       
        button= Button(text='Enviar', font_size=16, pos_hint={'center_x': 0.5, 'top': 0.3}, size_hint=(0.3, 0.1),color=(0, 0, 1, 1))
        box.add_widget(button)


        return box
    def incrementar(self,button):
        button.text='soltei'
InterFace().run()

    
