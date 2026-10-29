from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class KalkulatorModernHP(App):
    def build(self):
        # Mengatur warna latar belakang aplikasi (Abu-abu sangat gelap / Dark Mode)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        # Layout utama vertikal
        layout_utama = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Layar display kalkulator yang estetik
        self.layar = TextInput(
            text='0',
            multiline=False,
            readonly=True,
            halign='right',
            font_size=50,
            background_normal='',  # Menghilangkan border bawaan yang kaku
            background_color=(0.15, 0.15, 0.15, 1), # Warna layar kontras
            foreground_color=(1, 1, 1, 1),          # Warna teks putih
            size_hint_y=0.25
        )
        layout_utama.add_widget(self.layar)
        
        # Grid untuk tombol-tombol (4 kolom)
        grid_tombol = GridLayout(cols=4, spacing=10)
        
        # Susunan tombol beserta kode warnanya
        # Format: (Teks Tombol, Warna Background RGBA)
        warna_angka = (0.25, 0.25, 0.25, 1)    # Abu-abu gelap
        warna_operator = (1, 0.6, 0, 1)        # Oranye terang
        warna_fungsi = (0.6, 0.6, 0.6, 1)      # Abu-abu terang
        
        daftar_tombol = [
            ('C', warna_fungsi), ('(', warna_fungsi), (')', warna_fungsi), ('/', warna_operator),
            ('7', warna_angka),  ('8', warna_angka),  ('9', warna_angka),  ('*', warna_operator),
            ('4', warna_angka),  ('5', warna_angka),  ('6', warna_angka),  ('-', warna_operator),
            ('1', warna_angka),  ('2', warna_angka),  ('3', warna_angka),  ('+', warna_operator),
            ('.', warna_angka),  ('0', warna_angka),  ('=', warna_operator)
        ]
        
        # Membuat dan menghias tombol secara dinamis
        for teks, warna in daftar_tombol:
            # Khusus tombol '=' dibuat lebih lebar jika berada di baris akhir
            hint_x = 2 if teks == '=' else 1
            
            btn = Button(
                text=teks,
                font_size=28,
                background_normal='', # Menghilangkan style kotak kaku bawaan Kivy
                background_color=warna,
                color=(0, 0, 0, 1) if warna == warna_fungsi else (1, 1, 1, 1),
                size_hint_x=hint_x
            )
            
            # Menghubungkan fungsi klik
            if teks == '=':
                btn.bind(on_press=self.hitung_hasil)
            elif teks == 'C':
                btn.bind(on_press=self.hapus_layar)
            else:
                btn.bind(on_press=self.tombol_ditekan)
                
            grid_tombol.add_widget(btn)
            
        layout_utama.add_widget(grid_tombol)
        return layout_utama

    def tombol_ditekan(self, instance):
        if self.layar.text == '0' or self.layar.text == 'Error':
            self.layar.text = instance.text
        else:
            self.layar.text += instance.text

    def hapus_layar(self, instance):
        self.layar.text = '0'

    def hitung_hasil(self, instance):
        try:
            # Evaluasi ekspresi matematika langsung dari string
            hasil = str(eval(self.layar.text))
            self.layar.text = hasil
        except ZeroDivisionError:
            self.layar.text = 'Error: /0'
        except Exception:
            self.layar.text = 'Error'

if __name__ == '__main__':
    KalkulatorModernHP().run()
