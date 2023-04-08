#na biblioteca kivy tem diversos com ponentes para criar interfaces graficas o codigo abaixo adiciona a tela e os componentes.
from kivy.app import App
from kivy.uix.button import Button
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
        Fundo = Image(source='Fundo1.jpg', allow_stretch=True, keep_ratio=False)
        box.add_widget(Fundo)
        
#informação titulo 
        label_title=Label(text='Insira as informações químicas do rótulo do vinho:', font_size=20, halign='center', pos_hint={'center_x': 0.5, 'top': 1.47}, color=(1, 0, 0, 1))
        box.add_widget(label_title)
#informação de entrada
        label_alcool=Label(text='Álcool:', font_size=16, pos_hint={'right': 0.38, 'top': 0.9}, size_hint=(0.2, 0.05),color=(0, 0, 1, 1))
        box.add_widget(label_alcool)
#caixa de entrada onde o usuario digita as informaçoes neste caso alcool
        entrada_alcool=TextInput(multiline=False, font_size=16, pos_hint={'center_x': 0.5, 'top': 0.9}, size_hint=(0.3, 0.05))
        box.add_widget(entrada_alcool)
#informação de entrada
        label_Ph=Label(text='Ph:', font_size=16, pos_hint={'right': 0.38, 'top': 0.8}, size_hint=(0.2, 0.05),color=(0, 0, 1, 1))
        box.add_widget(label_Ph)
#caixa de entrada onde o usuario digita as informaçoes neste caso Ph
        entrada_Ph=TextInput(multiline=False, font_size=16, pos_hint={'center_x': 0.5, 'top': 0.8}, size_hint=(0.3, 0.05))
        box.add_widget(entrada_Ph)
#informação de entrada
        label_acidez=Label(text='Acidez Total:', font_size=16, pos_hint={'right': 0.38, 'top': 0.7}, size_hint=(0.2, 0.05),color=(0, 0, 1, 1))
        box.add_widget(label_acidez)
#caixa de entrada onde o usuario digita as informaçoes neste caso alcool
        entrada_acidez=TextInput(multiline=False, font_size=16, pos_hint={'center_x': 0.5, 'top': 0.7}, size_hint=(0.3,0.05))
        box.add_widget(entrada_acidez)
#informação de entrada
        label_acucar=Label(text='Açucar Residual:', font_size=16, pos_hint={'right': 0.37, 'top': 0.6}, size_hint=(0.2, 0.05),color=(0, 0, 1, 1))
        box.add_widget(label_acucar)
#caixa de entrada onde o usuario digita as informaçoes neste caso alcool
        entrada_acucar=TextInput(multiline=False, font_size=16, pos_hint={'center_x': 0.5, 'top': 0.6}, size_hint=(0.3, 0.05))
        box.add_widget(entrada_acucar)
#botao de enviar       
        button= Button(text='Enviar', font_size=20, pos_hint={'center_x': 0.5, 'top': 0.3}, size_hint=(0.15, 0.05),color=(0, 0, 139, 1),background_color = (0, 1, 1, 1))
        box.add_widget(button)

        return box
InterFace().run()

    
