from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from jnius import autoclass, cast
from android import mActivity

# Android sınıflarını yükle
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')

class SMSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.phone_number_input = TextInput(hint_text='Phone Number', multiline=False)
        self.phone_number_input.text = '+905395154570'  # Belirli bir numara ayarla
        
        self.message_input = TextInput(hint_text='Message', multiline=True)
        self.message_input.text = 'This is a test message'  # Varsayılan mesaj
        
        self.send_button = Button(text='Send 50 SMS')
        self.send_button.bind(on_press=self.send_50_sms)
        
        layout.add_widget(self.phone_number_input)
        layout.add_widget(self.message_input)
        layout.add_widget(self.send_button)
        
        return layout
    
    def send_50_sms(self, instance):
        phone_number = self.phone_number_input.text
        message = self.message_input.text
        
        if phone_number and message:
            for _ in range(50):
                self.send_sms(phone_number, message)
    
    def send_sms(self, phone_number, message):
        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(f"sms:{phone_number}"))
        intent.putExtra("sms_body", message)
        current_activity = cast('android.app.Activity', mActivity)
        current_activity.startActivity(intent)

if __name__ == '__main__':
    SMSApp().run()
