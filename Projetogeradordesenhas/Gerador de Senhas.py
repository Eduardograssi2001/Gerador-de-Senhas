import kivy
import random
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout

kivy.require('2.1.0')  # versão do Kivy

class PasswordGeneratorApp(App):
    def build(self):
        self.title = "Gerador de Senhas Seguras"
        
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        self.title_label = Label(text="Gerador de Senhas Seguras", font_size=24, size_hint=(1, 0.1))
        self.layout.add_widget(self.title_label)

        # Slider para selecionar o tamanho da senha
        self.length_label = Label(text="Tamanho da senha (8-32):", size_hint=(1, 0.1))
        self.layout.add_widget(self.length_label)

        self.password_length_slider = Slider(min=8, max=32, value=8, step=1, size_hint=(1, 0.1))
        self.password_length_slider.bind(value=self.on_slider_value_change)
        self.layout.add_widget(self.password_length_slider)

        # Exibição do tamanho selecionado
        self.length_value_label = Label(text="8", size_hint=(1, 0.1))
        self.layout.add_widget(self.length_value_label)

        # Opções de seleção
        self.options_layout = GridLayout(cols=2, size_hint=(1, 0.3))

        # Opção de incluir números
        self.include_numbers_switch = Switch(active=False)
        self.include_numbers_label = Label(text="Incluir Números", size_hint=(0.7, 1))
        self.options_layout.add_widget(self.include_numbers_label)
        self.options_layout.add_widget(self.include_numbers_switch)

        # Opção de incluir caracteres especiais
        self.include_specials_switch = Switch(active=False)
        self.include_specials_label = Label(text="Incluir Caracteres Especiais", size_hint=(0.7, 1))
        self.options_layout.add_widget(self.include_specials_label)
        self.options_layout.add_widget(self.include_specials_switch)

        # Opção de incluir letras maiúsculas
        self.include_uppercase_switch = Switch(active=False)
        self.include_uppercase_label = Label(text="Incluir Letras Maiúsculas", size_hint=(0.7, 1))
        self.options_layout.add_widget(self.include_uppercase_label)
        self.options_layout.add_widget(self.include_uppercase_switch)

        self.layout.add_widget(self.options_layout)

        # Botão para gerar a senha
        self.generate_button = Button(text="Gerar Senha", size_hint=(1, 0.1))
        self.generate_button.bind(on_press=self.generate_password)
        self.layout.add_widget(self.generate_button)

        # Exibição da senha gerada
        self.generated_password_label = Label(text="Senha gerada aparecerá aqui", font_size=20, size_hint=(1, 0.1))
        self.layout.add_widget(self.generated_password_label)

        return self.layout

    def on_slider_value_change(self, instance, value):
        self.length_value_label.text = str(int(value))

    def generate_password(self, instance):
        length = int(self.password_length_slider.value)
        use_numbers = self.include_numbers_switch.active
        use_specials = self.include_specials_switch.active
        use_uppercase = self.include_uppercase_switch.active

        # Gerar a senha
        password = self.create_password(length, use_numbers, use_specials, use_uppercase)
        self.generated_password_label.text = password

    def create_password(self, length, use_numbers, use_specials, use_uppercase):
        # Definir os caracteres disponíveis
        characters = string.ascii_lowercase  # Letras minúsculas
        
        if use_uppercase:
            characters += string.ascii_uppercase  # Letras maiúsculas
        if use_numbers:
            characters += string.digits  # Números
        if use_specials:
            characters += string.punctuation  # Caracteres especiais

        # Gerar a senha aleatória
        password = ''.join(random.choice(characters) for i in range(length))
        return password

if __name__ == '__main__':
    PasswordGeneratorApp().run()
