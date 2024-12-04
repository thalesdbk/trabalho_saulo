from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Tela de Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Campos de entrada
        self.username_input = TextInput(hint_text="Usuário", multiline=False)
        self.password_input = TextInput(hint_text="Senha", password=True, multiline=False)

        # Botão de login
        login_button = Button(text="Login", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        login_button.bind(on_press=self.validate_login)

        # Adicionar widgets ao layout
        layout.add_widget(Label(text="Bem-vindo à Loja de Roupas", font_size=24))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Validação simples (substitua por autenticação real)
        if username == "admin" and password == "1234":
            self.manager.current = "home"
        else:
            self.username_input.text = ""
            self.password_input.text = ""
            self.username_input.hint_text = "Usuário ou senha inválidos!"


# Tela Inicial (Home)
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Mensagem de boas-vindas
        welcome_label = Label(text="Bem-vindo à Loja!", font_size=24)

        # Botão para sair
        logout_button = Button(text="Sair", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        logout_button.bind(on_press=self.logout)

        layout.add_widget(welcome_label)
        layout.add_widget(logout_button)

        self.add_widget(layout)

    def logout(self, instance):
        self.manager.current = "login"


# Gerenciador de Telas
class LojaDeRoupasApp(App):
    def build(self):
        sm = ScreenManager()

        # Adicionar telas ao gerenciador
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))

        return sm


# Executar o aplicativo
if __name__ == "__main__":
    LojaDeRoupasApp().run()