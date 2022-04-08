import kivy
import os
#from tempfile import TemporaryFile
#from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.core.window import Window
from translate import Translator
from kivy.uix.image import Image
from gtts import gTTS
from io import BytesIO
#from kivy.core.audio import SoundLoader
import gtts
from playsound import playsound
'''from pydub import AudioSegment
from pydub.playback import play'''


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
       
      
class Trans(Screen):
    def __init__(self,**kwargs):
        super(Trans, self).__init__(**kwargs)
        
        #self.add_widget(Image(source="languages.png",size_hint=(0.1,0.1),pos=(350,520)))
        self.display=Label(text="TRANSLATED TEXT",font_name="comic.ttf",font_size=30,size_hint=(.3,.2),pos_hint={'x': .35, 'y': .4},color='#00008B')

        self.add_widget(Label(text='LANGUAGE',font_name="comic.ttf",font_size=18, text_size=(200,None), size_hint=(.7, .1), pos_hint={'x': .03, 'y': .85},color= '##183a1d'))
        self.Language = TextInput(multiline=False, size_hint=(.3, .1), pos_hint={'x': .44, 'y': .85})
        self.add_widget(self.Language)

        self.add_widget(Label(text='TEXT',font_name="comic.ttf",font_size=18, text_size=(200,None),size_hint=(.7, .1), pos_hint={'x': .03, 'y': .65},color= '#183a1d'))
        self.sample_text = TextInput(multiline=False, size_hint=(.3, .1), pos_hint={'x': .44, 'y': .65})
        self.add_widget(self.sample_text)

        self.btn = Button(text='TRANSLATE',font_name="comic.ttf",font_size=25, size_hint=(.3, .1), pos_hint={'x': .35, 'y': .25},background_color= '#B0554A')
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.submit)
        self.add_widget(self.display)

        self.speech=Button(text='AUDIO',font_name="comic.ttf",font_size=20,pos_hint={'x': .67, 'y': .25},size_hint=(.3,.1),background_color ='#B0554A')
        self.add_widget(self.speech)
        self.speech.bind(on_press=self.talk)

        self.btn3 = Button(text='<<--BACK',font_name="comic.ttf",font_size=20,size_hint= (0.3,0.1),bold= True,background_color ='#B0554A',pos_hint={'x': .03, 'y': .25})
        self.add_widget(self.btn3)
        self.btn3.bind(on_press = self.screen1_transition)
        

    def screen1_transition(self, *args):
        self.manager.current = 'login'
        
    def submit(self, instance):
        
        var=self.Language.text
        print(var)            
        translator= Translator(from_lang="English",to_lang=var)
        translation = translator.translate(self.sample_text.text)                    
            #print(translation)
        self.display.text=translation
        print(self.display.text)

    def talk(self,a):
        tts = gtts.gTTS(self.display.text, lang="hi")
        tts.save("audio.mp3")
        os.startfile("audio.mp3")
        
        '''tts = gTTS(self.display.text, lang='hi')
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        song=AudioSegment.from_file(fp,format="mp3")
        play(song)'''
        #playsound(tts.write_to_fp(mp3_fp))
        #tts = gTTS(text='Hello', lang='en')
        #f = TemporaryFile()
        #tts.write_to_fp(f)
        # Play f
        #f.close()             

        
        
class LoginWindow(Screen):
        def __init__(self, **kwargs):
            #Window.clearcolor=(200/250,218/250,221/250,200/250)
            Window.clearcolor=(255/250,229/250,180/250,0/250)
            super(LoginWindow, self).__init__(**kwargs)
            self.add_widget(Image(source="languages.png",size_hint=(0.2,0.4),pos_hint={'x': .4, 'y': .55}))
            self.label_on_screen=Label(text="TRANSLATOR",font_name="comic.ttf",font_size=30,size_hint=(.4,.8),pos_hint={'x': .28, 'y': .1},color='#183a1d')
            self.add_widget(self.label_on_screen)
            self.btn2 = Button(text='LETS BEGIN!!!',font_name="comic.ttf",size_hint= (0.5,0.12),bold= True,background_color ='#00FFCE',pos_hint={'x': .24, 'y': .25})
            self.add_widget(self.btn2)
            self.btn2.bind(on_press = self.screen_transition)
           
            

        def screen_transition(self, *args):
            self.manager.current = 'Trans'

class MyApp(App):    
    def build(self):
        
        
        sm = MyScreenManager(transition=FadeTransition())
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(Trans(name='Trans'))
        return sm

        
MyApp().run()
